# v 1.0.1
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

def link_validation(unique_link):
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

    req = urllib.request.Request(unique_link, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout = 15) as response:
            if response.code >= 200 or response.code <=399:
                print(
                    f'{unique_link}\n'
                    f'\t- Responded {GREEN}{response.status} {response.reason}{RESET}'
                )
            else:
                print(
                    f'{unique_link}\n'
                    f'\t- Unknown error {RED}[FAILED]{RESET}'
                )
                failed_links.append(unique_link)
    except urllib.error.HTTPError as e:
        print(
            f'{unique_link}\n'
            f'\t- Responded HTTP Error: {RED}{e.code} {e.reason}{RESET}'
        )
        failed_links.append(f'{unique_link} - {e.code} {e.reason}')
    except urllib.error.URLError as e:
        print(
            f'{unique_link}\n'
            f'\t- Responded URL Error: {RED}{e.reason}{RESET}'
        )
        failed_links.append(f'{unique_link} - {e.reason}')
    except TimeoutError as e:
        print(
            f'{unique_link}\n'
            f'\t- Responded {RED}Timeout Error{RESET}'
        )
        failed_links.append(f'{unique_link} - Timeout Error')

def main():
    """Validates links found in ProLUG Course-Books repo
        Returns per file total and total unique links found
        Then reports invalidated links to file

        Must be run from root of git repo directory
    """

    uniq_total = set()
    total_links = int(0)
    file_paths = Path('docs/').glob('**/*.md')

    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            contents = f.read()
            link_search = re.findall(REGEX, contents)
            list_sum = len(link_search)
            print(f'{ORANGE}File{RESET}: {path}\n{"-"*50}')
            if list_sum > 0:
                for link in link_search:
                    print(link)
                    uniq_total.add(link)
                total_links += list_sum
                print(f'\nLinks found: {BLUE}{list_sum}{RESET}\n')
            else:
                print('No links found...\n')
    print(f'Total links found: {ORANGE}{total_links}{RESET}')
    print(f'Unique links: {GREEN}{len(uniq_total)}{RESET}\n{"-"*50}')

    with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
        futures = {executor.submit(link_validation, url): url for url in uniq_total}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f'{futures[future]} -> Unexpected error: {e}')

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
