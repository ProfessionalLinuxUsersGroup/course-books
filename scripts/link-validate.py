# v 1.2.158
# Authored by Christian McKee - cmckee786@github.com
# Attempts to validate links within ProLUG Course-Books repo
# Must be called from root of github repo directory
# Not intended for use in runner builds for the time being

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
# Regex intended to match http(s) links unique to this project (very greedy)
REGEX = r"(?<!\[)https?:\/\/(?:\S+\.)[^\s\)\]\}\<\>\"\,]+"

STORAGE = 'scripts/link-storage/successfullinks.txt'
IGNORED = 'scripts/link-storage/ignoredlinks.txt'

stored_links: list = []
ignored_links: list = []
successful_links: list = []
failed_links: list = []


if Path(STORAGE).exists():
    with open(STORAGE, 'r', encoding='utf-8') as f_cur:
        stored_links = [line.strip() for line in f_cur]
else:
    with open(STORAGE, 'w', encoding = 'utf-8'):
        pass

if Path(IGNORED).exists():
    with open(IGNORED, 'r', encoding='utf-8') as f_cur:
        ignored_links = [line.strip() for line in f_cur]
else:
    with open(IGNORED, 'w', encoding = 'utf-8'):
        pass


def link_validation(matched_item: dict):
    """Utilizes user-agent headers lest webservers return false negative
       Odds are some requests may be blocked by rate limiters like Cloudflare
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
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

def link_processing():
    """Validates links found in ProLUG Course-Books repo
        Returns per file total and total unique links found
        Then reports invalidated links to file

        Must be run from root of git repo directory
    """

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
            print(f'{ORANGE}File{RESET}: {path}\n{"-"*50}')
            contents: list = f.read().splitlines()
            for i, line in enumerate(contents, 1):
                str_match = re.search(REGEX, line)
                if str_match:
                    print(f'{GREEN}L:{i}{RESET} | {str_match.group(0)}')
                    link_item = {
                        "link": str_match.group(0),
                        "file": f"{path}",
                        "line": i
                    }
                    matched_links.append(link_item)
                    file_matches += 1
            if file_matches == 0:
                print('No links found...\n')
            else:
                print(f'\nLinks found: {BLUE}{file_matches}{RESET}\n')
            total_links += file_matches
            file_matches = 0
    unique_links = list({i['link']:i for i in reversed(matched_links)}.values())

    print('Filtering stored and ignored links...\n')
    if stored_links:
        unique_links[:] = [d for d in unique_links if d['link'] not in stored_links]
        unique_links[:] = [d for d in unique_links if d['link'] not in ignored_links]

    print(f'Total links found: {ORANGE}{total_links}{RESET}')
    print(f'Links to Test: {GREEN}{len(unique_links)}{RESET}\n{"-"*50}')

    with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
        futures = {
            executor.submit(link_validation, dict_item):
            dict_item for dict_item in unique_links
        }
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f'{futures[future]} -> Unexpected error: {e}')

def main():
    """The place we call home"""
    link_processing()

    report = f"failed_links.{datetime.now().strftime('%Y-%m-%d')}"
    with open(report, 'w', encoding='utf-8') as f_report, \
         open(STORAGE, 'a', encoding='utf-8') as f_updated:
        print(
            f'Failed Links: {RED}{len(failed_links)}{RESET}\n'
            f'Writing report to {Path.cwd()}/{report}...'
        )
        f_report.write(f'Report ran on: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n{"-"*50}\n')
        if failed_links:
            [f_report.writelines(f'{link}\n') for link in failed_links]
        if successful_links:
            [f_updated.writelines(f'{link}\n') for link in successful_links]

if __name__ == '__main__':
    main()
