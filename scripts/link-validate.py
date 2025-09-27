# v 1.5.103
# Authored by Christian McKee - cmckee786@github.com
# Attempts to validate links within ProLUG Course-Books repo

# Likely will not match 100% of links, edge cases will need to
# be added to ignoredlinks.txt. Additionally attempts to store
# validated links in flat file to reduce subsequent runtimes

# Must be called from root of github repo directory
# Not intended for use in runner builds for the time being
# Delete successfullinks.txt for now to retest all links

import re
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[34m"
ORANGE = "\033[33m"
RESET = "\033[0m"

# Worker count dependent on host limitations
WORKER_COUNT = 20
# Regex intended to match http(s) links unique to this project
REGEX = r"(?<!\[)https?://\S+[^\s\.\"\'\,\>\)\{\}]"
pattern = re.compile(REGEX)

STORAGE = 'scripts/link-storage/successfullinks.txt'
IGNORED = 'scripts/link-storage/ignoredlinks.txt'

successful_links: list = []
failed_links: list = []

def file_setup(path: str):
    """Instantiate files if missing, and populate stored/ignored links"""
    if Path(path).exists():
        with open(path, 'r', encoding='utf-8') as f_stored:
            stored_links: list = [line.strip() for line in f_stored]
    else:
        with open(path, 'w', encoding = 'utf-8'):
            stored_links = []

    return stored_links

def file_processing(path: str):
    """Sort files for stored and ignored links to reduce diffs"""
    with open(path, 'r', encoding='utf-8') as f_pre:
        links: list = [line.strip() for line in f_pre]
        links.sort()
        if links:
            with open(path, 'w', encoding='utf-8') as f_post:
                for line in links:
                    f_post.writelines(f'{line}\n')

def link_validation(matched_item: dict):
    """Utilizes user-agent headers lest webservers return false negatives
       Odds are some requests may be blocked by rate limiters like Cloudflare
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/143.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

    req = urllib.request.Request(matched_item["link"], headers=headers)
    troubleshoot_output = f' {ORANGE}File:{RESET}{matched_item["file"]}'\
                          f' {BLUE}L:{matched_item["line"]} {RESET}'

    try:
        with urllib.request.urlopen(req, timeout = 7) as response:
            if response.code >= 200 or response.code <=399:
                print(
                    f'{matched_item['link']}\n'
                    f'\t- Responded {GREEN}{response.status} {response.reason}{RESET}'
                )
                successful_links.append(matched_item['link'])
            else:
                print(
                    f'{matched_item['link']}\n'
                    f'\t- Unknown error {RED}[FAILED]{RESET}'
                )
                failed_links.append(
                    f'{matched_item["link"]}{troubleshoot_output}'
                )
    except urllib.error.HTTPError as e:
        print(
            f'{matched_item["link"]}\n'
            f'\t- Responded HTTP Error: {RED}{e.code} {e.reason}{RESET}'
        )
        failed_links.append(
            f'{matched_item['link']} - {RED}{e.code} {e.reason}{RESET}{troubleshoot_output}'
        )
    except urllib.error.URLError as e:
        print(
            f'{matched_item['link']}\n'
            f'\t- Responded URL Error: {RED}{e.reason}{RESET}'
        )
        failed_links.append(
            f'{matched_item['link']} - {RED}{e.reason}{RESET}{troubleshoot_output}'
        )
    except TimeoutError as e:
        print(
            f'{matched_item['link']}\n'
            f'\t- Responded {RED}Timeout Error{RESET}'
        )
        failed_links.append(
            f'{matched_item['link']} - {RED}Timeout Error{RESET}{troubleshoot_output}'
        )

def link_processing(stored: list, ignored: list):
    """Attemptes to validate links found in ProLUG Course-Books repo
        Returns per file total and total unique links found
        Must be run from root of git repo directory
    """

    stored_links: list = stored
    ignored_links: list = ignored
    matched_links: list = []
    unique_links: list = []
    file_matches: int = 0
    total_links: int = 0
    file_paths = Path('docs/').glob('**/*.md')
    link_item: dict = {
        "link": "",
        "file": "",
        "line": ""
    }

    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            print(f'{ORANGE}File{RESET}:{path}\n{"-"*50}')
            contents: list = f.read().splitlines()
            for i, line in enumerate(contents, 1):
                str_match = pattern.search(line)
                if str_match:
                    match: str = str_match.group(0)
                    if '(' in match and 'localhost' not in match:
                        match = match + ')'
                    elif 'localhost' in match :
                        match = ''
                else:
                    match = ''
                if match:
                    print(f'{GREEN}L:{i}{RESET} | {match}')
                    link_item = {
                        "link": match,
                        "file": f"{path}",
                        "line": i
                    }
                    matched_links.append(link_item)
                    file_matches += 1
            if file_matches == 0:
                print('No links found...')
            print()
            total_links += file_matches
            file_matches = 0

    unique_links = list({i['link']:i for i in reversed(matched_links)}.values())

    print(f'Total links found: {ORANGE}{total_links}{RESET}\n')
    print('Filtering stored and ignored links...\n')

    if stored_links:
        unique_links[:] = [d for d in unique_links if d['link'] not in stored_links]
        unique_links[:] = [d for d in unique_links if d['link'] not in ignored_links]

    print(f'\nLinks to Test: {GREEN}{len(unique_links)}{RESET}\n{"-"*50}')
    for _ in unique_links:
        print(f"{_['link']} {ORANGE}File:{RESET} {_['file']} {BLUE}L:{_['line']}{RESET}")

    return unique_links

def main():
    """The place we call home"""

    try:
        storage_links = file_setup(STORAGE)
        ignored_storage_links = file_setup(IGNORED)
        test_links = link_processing(storage_links, ignored_storage_links)

        if test_links:
            print(f'\nFetching links\n{"-"*50}')
            with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
                futures = {
                    executor.submit(link_validation, dict_item):
                    dict_item for dict_item in test_links
                }
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        print(f'{futures[future]} -> Unexpected error: {e}')

            report = f"failed_links.{datetime.now().strftime('%Y-%m-%d')}"
            with open(report, 'w', encoding='utf-8') as f_report, \
                 open(STORAGE, 'a', encoding='utf-8') as f_updated:
                print(
                    f'\nFailed Links: {RED}{len(failed_links)}{RESET}\n'
                    f'Writing report to {Path.cwd()}/{report}...'
                )
                f_report.write(f'Report ran on: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n{"-"*50}\n')
                if failed_links:
                    [f_report.writelines(f'{link}\n') for link in failed_links]

                if successful_links:
                    [f_updated.writelines(f'{link}\n') for link in successful_links]

    except Exception as e:
        print(e)
    finally:
        if Path(STORAGE).exists():
            file_processing(STORAGE)
        if Path(IGNORED).exists():
            file_processing(IGNORED)

if __name__ == '__main__':
    main()
