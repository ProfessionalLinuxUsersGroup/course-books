# v 1.8.8
# Authored by Christian McKee - cmckee786@github.com
# Attempts to validate links within ProLUG Course-Books repo

# Likely will not match 100% of links, edge cases will need to
# be added to ignoredlinks.txt. Additionally attempts to store
# validated links in flat file to reduce subsequent runtimes

# Not intended for use in runner or automated builds

# USE RESPONSIBLY

import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

RED: str = "\033[91m"
GREEN: str = "\033[92m"
BLUE: str = "\033[34m"
ORANGE: str = "\033[33m"
RESET: str = "\033[0m"

# If max_workers is None or not given, it will default
# to the number of processors on the machine, multiplied by 5
WORKER_COUNT = 10

# Regex intended to match http(s) links unique to this project
REGEX: str = r"(?<!\[)\bhttps?://\S+\b/?"
PATTERN: re.Pattern = re.compile(REGEX)

CWD: Path = Path.cwd()
FAILED_REPORT_PATH: Path = Path(f"{CWD}/failed_links.{datetime.now().strftime('%Y-%m-%d')}")
STORAGE_PATH: Path = Path(f"{CWD}/scripts/link-storage/successfullinks.txt")
IGNORED_PATH: Path = Path(f"{CWD}/scripts/link-storage/ignoredlinks.txt")


def cli_args() -> argparse.ArgumentParser:
    """CLI options to skip validated or ignored link storage and more
    Create and return argparse object with configured argument attributes
    """
    args_parser = argparse.ArgumentParser(
        description="Attempts to resolve any http(s) URL links found recursively "
        "from execution path. Stores successfully resolved links to "
        "'scripts/link-storage/successfullinks.txt' by default."
    )
    args_parser.add_argument(
        "-s",
        "--skip-storage",
        action="store_true",
        help="skip inclusion of stored successfullinks.txt URLs",
        dest="skip_store",
    )
    args_parser.add_argument(
        "-i",
        "--skip-ignored",
        action="store_true",
        help="skip inclusion of stored ignoredlinks.txt URLs",
        dest="skip_ignore",
    )
    args_parser.add_argument(
        "-r",
        "--build-storage",
        action="store_true",
        help="build new successfullinks.txt file based on resolved links",
        dest="build_storage",
    )
    args_parser.add_argument(
        "-b",
        "--build-ignored",
        action="store_true",
        help="build new ignorelinks.txt file based on reported failed links",
        dest="build_ignore",
    )
    args_parser.add_argument(
        "-a",
        "--add-failed",
        action="store_true",
        help="add failed links to ignorelinks.txt file",
        dest="add_failed",
    )
    args_parser.add_argument(
        "-n",
        "--no-validation",
        action="store_true",
        help="skip validation of URLs and print default reporting to stdout",
        dest="skip_validation",
    )
    args_parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default=CWD,
        help="aggregate links from a specified directory",
        dest="directory",
    )

    return args_parser


def get_file_links(path: Path) -> list[str | None]:
    """Populate stored/ignored links from passed path or instantiate file from path if missing"""
    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as f_stored:
            stored_links = [line.strip() for line in f_stored]
    else:
        with open(path, "w", encoding="utf-8"):
            stored_links: list = []

    return stored_links


def sort_file(path: Path) -> None:
    """Sort files for stored and ignored links to reduce diffs"""
    with open(path, "r", encoding="utf-8") as f_pre:
        links = [line.strip() for line in f_pre]
        links.sort()
        if links:
            with open(path, "w", encoding="utf-8") as f_post:
                for line in links:
                    f_post.writelines(f"{line}\n")


def validate_link(matched_item: dict[str, str | int | Path]) -> tuple:
    """Attempt to resolve link and return error or status code for processing
    Utilizes user-agent headers to reduce false negative returns
    """
    headers: dict = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/143.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }

    # Link assumed successful initially
    link_status: tuple = (0, "")
    dict_link: str = str(matched_item["link"])

    try:
        req = urllib.request.Request(dict_link, headers=headers)
        urllib.request.urlopen(req, timeout=7)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
        link_status = 1, e
    return link_status, matched_item


def get_unique_links(
    stored: list[str | None], ignored: list[str | None], arg_path: Path
) -> list:
    """Aggregate URLs for link validation into dictionary for processing
    Returns per file total and total unique links found into list for reporting
    """

    stored_links: list = stored
    ignored_links: list = ignored
    file_paths: list = []
    matched_links: list = []
    unique_links: list = []
    file_matches: int = 0
    total_links: int = 0
    link_item: dict[str, str | Path | int] = {"link": "", "file": "", "line": ""}

    # Traverse implied current or specified directory from argument
    for p in Path(arg_path).rglob("*"):
        try:
            if p.is_file() and p not in [
                Path(STORAGE_PATH),
                Path(IGNORED_PATH),
                Path(FAILED_REPORT_PATH),
            ]:
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
        # Skip non-text files
        except UnicodeDecodeError:
            pass

    # Filter for unique links
    unique_links = list({i["link"]: i for i in reversed(matched_links)}.values())

    print(
        f"Total links found: {ORANGE}{total_links}{RESET}\n"
        f"Unique links: {GREEN}{len(unique_links)}{RESET}\n"
        f"Filtering stored and ignored links..."
    )

    # Filter out ignored and stored links if available
    if stored_links:
        unique_links[:] = [d for d in unique_links if d["link"] not in stored_links]
    if ignored_links:
        unique_links[:] = [d for d in unique_links if d["link"] not in ignored_links]

    return unique_links


def main() -> None:
    """The place we call home"""
    arg_path: Path
    successful_links: list = []
    failed_links: list = []
    storage_links: list = []
    ignored_storage_links: list = []

    try:
        parser = cli_args().parse_args()

        if parser.build_ignore:
            print("Ignored link storage has been reset...")
            with open(IGNORED_PATH, "w", encoding="utf-8"):
                pass
        if parser.build_storage:
            print("Successful link storage has been reset...")
            with open(STORAGE_PATH, "w", encoding="utf-8"):
                pass
        if parser.skip_store is False:
            storage_links = get_file_links(STORAGE_PATH)
        if parser.skip_ignore is False:
            ignored_storage_links = get_file_links(IGNORED_PATH)
        if parser.directory and Path(parser.directory).exists():
            arg_path = parser.directory
        else:
            print("Path may not exist\nExiting...")
            sys.exit(1)

        test_links = get_unique_links(storage_links, ignored_storage_links, arg_path)

        if test_links and parser.skip_validation is False:
            print("Attempting to resolve links for testing...")
            count: int = 0
            with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
                futures = {
                    executor.submit(validate_link, dict_item): dict_item
                    for dict_item in test_links
                }
                for future in as_completed(futures):
                    try:
                        validate_return, matched_item = future.result()
                        if validate_return[0] == 1:
                            failed_links.append((matched_item, validate_return))
                            count += 1
                        elif validate_return[0] == 0:
                            successful_links.append(matched_item)
                            count += 1
                        print(
                            f"\rTesting links: {ORANGE}{count}{RESET}|{len(test_links)} "
                            f"{(int(count/len(test_links) * 100)):.0f}%",
                            end="",
                            flush=True,
                        )
                    except Exception as e:
                        print(f"{futures[future]} - Unexpected error: {e}")
        print()

        if successful_links and parser.skip_store is False:
            print(f"Appending successful links to {STORAGE_PATH}...")
            with open(STORAGE_PATH, "a", encoding="utf-8") as f_updated:
                [f_updated.writelines(f'{link["link"]}\n') for link in successful_links]
            sort_file(STORAGE_PATH)

        if failed_links and parser.skip_validation is False:
            print(f"Failed Links: {RED}{len(failed_links)}{RESET}")
            print(f"{'-'*20}")
            [
                print(f"{item[0]['link']} {RED}{item[1][1]}{RESET}")
                for item in failed_links
            ]
            print(f"{'-'*20}")
            print(f"Writing report to {FAILED_REPORT_PATH}...")
            with open(FAILED_REPORT_PATH, "w", encoding="utf-8") as f_report:
                [
                    f_report.writelines(
                        f"{item[0]['link']}"
                        f" {ORANGE}File:{item[0]['file']}{RESET}"
                        f" {BLUE}L:{item[0]['line']}{RESET}"
                        f" {RED}{item[1][1]}{RESET}\n"
                    )
                    for item in failed_links
                ]

            if parser.build_ignore:
                print(f"Building new {IGNORED_PATH} file...")
                with open(IGNORED_PATH, "w", encoding="utf-8") as f_ignore:
                    [f_ignore.writelines(f'{link["link"]}\n') for link in failed_links]
                sort_file(IGNORED_PATH)

            if parser.add_failed and parser.build_ignore is False:
                print(f"Appending failed links to {IGNORED_PATH} file...")
                with open(IGNORED_PATH, "a", encoding="utf-8") as f_ignore:
                    [f_ignore.writelines(f'{link["link"]}\n') for link in failed_links]
                sort_file(IGNORED_PATH)

        elif parser.skip_validation is True:
            print("Skipped link validation!")
        else:
            print("No failed links!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
