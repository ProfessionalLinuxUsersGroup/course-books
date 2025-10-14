# v 1.6.4
# Authored by Christian McKee - cmckee786@github.com
# Attempts to validate links within ProLUG Course-Books repo

# Likely will not match 100% of links, edge cases will need to
# be added to ignoredlinks.txt. Additionally attempts to store
# validated links in flat file to reduce subsequent runtimes

# Must be called from root of github repo directory
# Not intended for use in runner builds for the time being
# Delete or empty successfullinks.txt for now to retest all links

# USE RESPONSIBLY

import re
import argparse
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

# If max_workers is None or not given, it will default
# to the number of processors on the machine, multiplied by 5
WORKER_COUNT = None

# Regex intended to match http(s) links unique to this project
REGEX = r"(?<!\[)\bhttps?://\S+\b/?"
PATTERN = re.compile(REGEX)

STORAGE = 'scripts/link-storage/successfullinks.txt'
IGNORED = 'scripts/link-storage/ignoredlinks.txt'


def cli_args():
    """ Provide CLI options to skip validated or ignored link storage and skip URL validation
        Create and return argparse object with configured argument attributes
    """

    args_parser = argparse.ArgumentParser(
        description='''
            Attempts to parse any http(s) URL links found within docs/**/*.md project directory and stores
            successfully validated URLs to reduce subsequent script executions. Reads from
            scripts/link-storage/successfullinks.txt and scripts/link-storage/ignoredlinks.txt to reduce
            subsequent runtimes and any user define URLs they wish to ignore.
            '''
    )
    args_parser.add_argument(
        '-s', '--skip-storage',
        action='store_true',
        help='Skip inclusion of stored successfullinks.txt URLs',
        dest='skip_store'
    )
    args_parser.add_argument(
        '-i', '--skip-ignored',
        action='store_true',
        help='Skip inclusion of stored ignoredlinks.txt URLs',
        dest='skip_ignore'
    )
    args_parser.add_argument(
        '-n', '--no-validation',
        action='store_true',
        help='Skip validation of URLs and print default reporting to stdout',
        dest='skip_validation'
    )

    return args_parser

def get_file_links(path: str):
    """Populate stored/ignored links from passed path or instantiate file from path if missing"""
    if Path(path).exists():
        with open(path, 'r', encoding='utf-8') as f_stored:
            stored_links: list = [line.strip() for line in f_stored]
    else:
        with open(path, 'w', encoding = 'utf-8'):
            stored_links = []

    return stored_links

def sort_file(path: str):
    """Sort files for stored and ignored links to reduce diffs"""
    with open(path, 'r', encoding='utf-8') as f_pre:
        links: list = [line.strip() for line in f_pre]
        links.sort()
        if links:
            with open(path, 'w', encoding='utf-8') as f_post:
                for line in links:
                    f_post.writelines(f'{line}\n')

def validate_link(matched_item: dict):
    """ Attempt to resolve link and return error or status code for processing
        Utilizes user-agent headers to reduce false negative returns
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/143.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

    link_status: tuple = ()
    req = urllib.request.Request(matched_item["link"], headers=headers)

    try:
        with urllib.request.urlopen(req, timeout = 7) as response:
            if response.code >= 200 or response.code <=399:
                print(
                    f'{matched_item['link']}\n'
                    f'\t- Responded {GREEN}{response.status} {response.reason}{RESET}'
                )
                link_status = 0, response.status
            else:
                print(
                    f'{matched_item['link']}\n'
                    f'\t- {RED}Unknown error{RESET}'
                )
                link_status = 1, 'Unknown Error'
    except urllib.error.HTTPError as e:
        print(
            f'{matched_item["link"]}\n'
            f'\t- Responded HTTP Error: {RED}{e.code} {e.reason}{RESET}'
        )
        link_status = 1, e
    except urllib.error.URLError as e:
        print(
            f'{matched_item['link']}\n'
            f'\t- Responded URL Error: {RED}{e.reason}{RESET}'
        )
        link_status = 1, e
    except TimeoutError as e:
        print(
            f'{matched_item['link']}\n'
            f'\t- Responded {RED}Timeout Error{RESET}'
        )
        link_status = 1, e

    return link_status, matched_item

def get_unique_links(stored: list, ignored: list):
    """ Aggregate URLs for link validation into dictionary for processing
        Returns per file total and total unique links found into list for reporting
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
                str_match = PATTERN.search(line)
                if str_match:
                    match: str = str_match.group(0)
                    if '(' in match and 'localhost' not in match:
                        split_match = match.split('/')
                        if '(' in split_match[-1] and ')' not in split_match[-1]:
                            split_match[-1] = split_match[-1] + ')'
                            match = '/'.join(split_match)
                    elif 'localhost' in match :
                        match = ''
                else:
                    match = ''
                if match:
                    link_item = {
                        "link": match,
                        "file": path,
                        "line": i
                    }
                    matched_links.append(link_item)
                    file_matches += 1
                    print(f'{BLUE}{file_matches}{RESET} | {GREEN}L:{i}{RESET} | {match}')
            if file_matches == 0:
                print('No links found...\n')
            else:
                print()
            total_links += file_matches
            file_matches = 0

    unique_links = list({i['link']:i for i in reversed(matched_links)}.values())

    print(
        f'Total links found: {ORANGE}{total_links}{RESET}\n'
        f'Unique links: {GREEN}{len(unique_links)}{RESET}\n'
        f'Filtering stored and ignored links...\n'
    )

    if stored_links:
        unique_links[:] = [d for d in unique_links if d['link'] not in stored_links]
    if ignored_links:
        unique_links[:] = [d for d in unique_links if d['link'] not in ignored_links]


    return unique_links

def main():
    """The place we call home"""
    try:
        cur_time =datetime.now().strftime('%Y-%m-%d')
        report = f"failed_links.{cur_time}"
        parser = cli_args().parse_args()
        successful_links: list = []
        failed_links: list = []

        if parser.skip_store is False:
            storage_links = get_file_links(STORAGE)
        else:
            storage_links = []
        if parser.skip_ignore is False:
            ignored_storage_links = get_file_links(IGNORED)
        else:
            ignored_storage_links = []
        test_links = get_unique_links(storage_links, ignored_storage_links)

        if test_links and parser.skip_validation is False:
            print(f'Attempting to resolve links for testing...\n{"-"*50}')
            with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
                futures = {
                    executor.submit(validate_link, dict_item):
                    dict_item for dict_item in test_links
                }
                for future in as_completed(futures):
                    try:
                        link_status, link = future.result()
                        troubleshoot_output: str = \
                                f'{link['link']}'\
                                f' {RED}{link_status[1]}{RESET}'\
                                f' {ORANGE}File:{RESET}{link["file"]}'\
                                f' {BLUE}L:{link["line"]}{RESET}'

                        if link_status[0] == 1:
                            failed_links.append(troubleshoot_output)
                        else:
                            successful_links.append(link['link'])
                    except Exception as e:
                        print(f'{futures[future]} - Unexpected error: {e}')

        if failed_links and parser.skip_validation is False:
            print(f'\nFailed Links: {RED}{len(failed_links)}{RESET}\n{"-"*50}')
            [print(item) for item in failed_links]
            print(f'\nWriting report to {Path.cwd()}/{report}...')
            with open(report, 'w', encoding='utf-8') as f_report:
                f_report.write(f'Report ran on: {cur_time}\n{"-"*50}\n')
                [f_report.writelines(f'{link}\n') for link in failed_links]
        elif parser.skip_validation is True:
            print('Skipped link validation!')
        else:
            print('No failed links!')

        if successful_links and parser.skip_store is False:
            with open(STORAGE, 'a', encoding='utf-8') as f_updated:
                [f_updated.writelines(f'{link}\n') for link in successful_links]
            sort_file(STORAGE)

    except Exception as e:
        print(e)
    finally:
        sort_file(IGNORED)

if __name__ == '__main__':
    main()
