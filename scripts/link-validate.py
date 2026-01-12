# v 1.8.1
# Authored by Christian McKee - cmckee786@github.com
# Attempts to validate links within ProLUG Course-Books repo

# Likely will not match 100% of links, edge cases will need to
# be added to ignoredlinks.txt. Additionally attempts to store
# validated links in flat file to reduce subsequent runtimes

# Not intended for use in runner builds for the time being

# USE RESPONSIBLY

import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

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

FAILED_REPORT = f"failed_links.{datetime.now().strftime('%Y-%m-%d')}"
STORAGE = "scripts/link-storage/successfullinks.txt"
IGNORED = "scripts/link-storage/ignoredlinks.txt"


def cli_args():
    """Provide CLI options to skip validated or ignored link storage and skip URL validation
    Create and return argparse object with configured argument attributes
    """
    args_parser = argparse.ArgumentParser(
        description="Attempts to resolve any http(s) URL links found recursively from execution path.",
    )
    args_parser.add_argument(
        "-s",
        "--skip-storage",
        action="store_true",
        help="Skip inclusion of stored successfullinks.txt URLs",
        dest="skip_store",
    )
    args_parser.add_argument(
        "-i",
        "--skip-ignored",
        action="store_true",
        help="Skip inclusion of stored ignoredlinks.txt URLs",
        dest="skip_ignore",
    )
    args_parser.add_argument(
        "-r",
        "--build-storage",
        action="store_true",
        help="Build new successfullinks.txt file based on resolved links",
        dest="build_storage",
    )
    args_parser.add_argument(
        "-b",
        "--build-ignored",
        action="store_true",
        help="Build new ignorelinks.txt file based on reported failed links",
        dest="build_ignore",
    )
    args_parser.add_argument(
        "-a",
        "--add-failed",
        action="store_true",
        help="Add failed links to ignorelinks.txt file",
        dest="add_failed",
    )
    args_parser.add_argument(
        "-n",
        "--no-validation",
        action="store_true",
        help="Skip validation of URLs and print default reporting to stdout",
        dest="skip_validation",
    )
    args_parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default=Path.cwd(),
        help="Aggregate links from a specified directory",
        dest="directory",
    )

    return args_parser


def get_file_links(path):
    """Populate stored/ignored links from passed path or instantiate file from path if missing"""
    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as f_stored:
            stored_links = [line.strip() for line in f_stored]
    else:
        with open(path, "w", encoding="utf-8"):
            stored_links = []

    return stored_links


def sort_file(path):
    """Sort files for stored and ignored links to reduce diffs"""
    with open(path, "r", encoding="utf-8") as f_pre:
        links = [line.strip() for line in f_pre]
        links.sort()
        if links:
            with open(path, "w", encoding="utf-8") as f_post:
                for line in links:
                    f_post.writelines(f"{line}\n")


def validate_link(matched_item):
    """Attempt to resolve link and return error or status code for processing
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

    link_status = ()
    req = urllib.request.Request(matched_item["link"], headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=7) as response:
            if response.code >= 200 or response.code <= 399:
                link_status = 0, response.status
            else:
                print(f"{matched_item['link']}\n" f"\t- {RED}Unknown error{RESET}")
                link_status = 1, "Unknown Error"
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
        link_status = 1, e

    return link_status, matched_item


def get_unique_links(stored, ignored, arg_path):
    """Aggregate URLs for link validation into dictionary for processing
    Returns per file total and total unique links found into list for reporting
    """

    stored_links = stored
    ignored_links = ignored
    file_paths = []
    matched_links = []
    unique_links = []
    file_matches = int(0)
    total_links = int(0)
    link_item = {"link": "", "file": "", "line": ""}

    for p in Path(arg_path).rglob("*"):
        try:
            if p.is_file() and p not in {
                Path(STORAGE),
                Path(IGNORED),
                Path(FAILED_REPORT),
            }:
                file_paths.append(p)
            else:
                continue
        except PermissionError:
            pass

    for path in file_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                contents = f.read().splitlines()
                for i, line in enumerate(contents, 1):
                    str_match = PATTERN.search(line)
                    if str_match:
                        match = str_match.group(0)
                        # Some URLs have nested resource URIs with parenthesis
                        # i.e: https://en.wikipedia.org/wiki/C_(programming_language)
                        if "(" in match and "localhost" not in match:
                            split_match = match.split("/")
                            if "(" in split_match[-1] and ")" not in split_match[-1]:
                                split_match[-1] = split_match[-1] + ")"
                                match = "/".join(split_match)
                        elif "localhost" in match:
                            match = ""
                    else:
                        match = ""
                    if match:
                        link_item = {"link": match, "file": path, "line": i}
                        matched_links.append(link_item)
                        file_matches += 1
                total_links += file_matches
                file_matches = 0
        except UnicodeDecodeError:
            pass

    unique_links = list({i["link"]: i for i in reversed(matched_links)}.values())

    print(
        f"Total links found: {ORANGE}{total_links}{RESET}\n"
        f"Unique links: {GREEN}{len(unique_links)}{RESET}\n"
        f"Filtering stored and ignored links..."
    )

    if stored_links:
        unique_links[:] = [d for d in unique_links if d["link"] not in stored_links]
    if ignored_links:
        unique_links[:] = [d for d in unique_links if d["link"] not in ignored_links]

    return unique_links


def main():
    """The place we call home"""
    arg_path = ()
    successful_links = []
    failed_links = []
    storage_links = []
    ignored_storage_links = []

    try:
        parser = cli_args().parse_args()

        if parser.build_ignore:
            print("Ignored link storage has been reset...")
            open(IGNORED, "w", encoding="utf-8").close()
        if parser.build_storage:
            print("Successful link storage has been reset...")
            open(STORAGE, "w", encoding="utf-8").close()
        if parser.skip_store is False:
            storage_links = get_file_links(STORAGE)
        if parser.skip_ignore is False:
            ignored_storage_links = get_file_links(IGNORED)
        if parser.directory and Path(parser.directory).exists():
            arg_path = parser.directory
        else:
            print("Path may not exist\nExiting...")
            sys.exit(1)

        test_links = get_unique_links(storage_links, ignored_storage_links, arg_path)

        if test_links and parser.skip_validation is False:
            print("Attempting to resolve links for testing...")
            print(f"Links to test: {BLUE}{len(test_links)}{RESET}\nPlease wait...")
            count = 0
            with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
                futures = {
                    executor.submit(validate_link, dict_item): dict_item
                    for dict_item in test_links
                }
                for future in as_completed(futures):
                    try:
                        link_status, link = future.result()
                        if link_status[0] == 1:
                            failed_links.append(link)
                            count += 1
                        elif link_status[0] == 0:
                            successful_links.append(link)
                            count += 1
                        print(
                            f"\rLinks tested: {ORANGE}{count}{RESET}",
                            end="",
                            flush=True,
                        )
                    except Exception as e:
                        print(f"{futures[future]} - Unexpected error: {e}")

            print()
        if successful_links and parser.skip_store is False:
            print("Appending successful links...")
            with open(STORAGE, "a", encoding="utf-8") as f_updated:
                [f_updated.writelines(f'{link["link"]}\n') for link in successful_links]
            sort_file(STORAGE)

        if failed_links and parser.skip_validation is False:
            print(f"Failed Links: {RED}{len(failed_links)}{RESET}")
            print(f"Writing report to {Path.cwd()}/{FAILED_REPORT}...")
            with open(FAILED_REPORT, "w", encoding="utf-8") as f_report:
                [
                    f_report.writelines(
                        f'{link["link"]}'
                        f' {ORANGE}File:{link["file"]}{RESET}'
                        f' {BLUE}L:{link["line"]}{RESET}\n'
                    )
                    for link in failed_links
                ]

            if parser.build_ignore:
                print("Building new ignoredlinks.txt file...")
                with open(IGNORED, "w", encoding="utf-8") as f_ignore:
                    [f_ignore.writelines(f'{link["link"]}\n') for link in failed_links]
                sort_file(IGNORED)

            if parser.add_failed and parser.build_ignore is False:
                print("Appending failed links to ignoredlinks.txt file...")
                with open(IGNORED, "a", encoding="utf-8") as f_ignore:
                    [f_ignore.writelines(f'{link["link"]}\n') for link in failed_links]
                sort_file(IGNORED)


        elif parser.skip_validation is True:
            print("Skipped link validation!")
        else:
            print("No failed links!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
