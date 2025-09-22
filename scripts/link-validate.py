# v 1.1.87
# Authored by Christian McKee - cmckee786@github.com
# Attempts to validate links within ProLUG Course-Books repo
# Must be called from root of github repo directory
# Not intended for use in runner builds for the time being

import re
from datetime import datetime
import urllib.request
import urllib.error
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

failed_links = []

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

    matched_links = []
    unique_links = []
    file_matches = int(0)
    total_links = int(0)
    file_paths = Path('docs/').glob('**/*.md')
    link_item = {
        "link": "",
        "file": "",
        "line": ""
    }

    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            print(f'{ORANGE}File{RESET}: {path}\n{"-"*50}')
            contents = f.read().splitlines()
            for i, line in enumerate(contents, 1):
                str_match = re.search(REGEX, line)
                if str_match:
                    print(f'{GREEN}L:{i}{RESET} | {str_match.group(0)}')
                    link_item = {
                        "link": str_match.group(0),
                        "file": f"{path.parent}/{path.name}",
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

    print(f'Total links found: {ORANGE}{total_links}{RESET}')
    print(f'Unique links: {GREEN}{len(unique_links)}{RESET}\n{"-"*50}')

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
    with open(
        report,
        'a',
        encoding='utf-8') as f:

        print(f'Writing report to {Path.cwd()}/{report}...')
        f.write(f'Report ran on: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n{"-"*50}\n')
        [f.writelines(f'{link}\n') for link in failed_links]

if __name__ == '__main__':
    main()
