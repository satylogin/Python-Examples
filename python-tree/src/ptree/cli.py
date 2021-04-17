from ptree.generators.tree_generator import TreeGenerator
from ptree.rptree import DirectoryTree
import argparse
import pathlib
import sys
from termcolor import colored

ERROR_BANNER = colored("ERROR:", "red")


def parse_args():
    parser = argparse.ArgumentParser(
        prog="ptree",
        description="print tree representation of dir",
        epilog="Thanks for using P Tree!",
    )
    parser.add_argument(
        "dir",
        metavar="ROOT_DIR",
        default=".",
        nargs="?",
        help="Generate a full directory tree starting at ROOT_DIR.",
    )
    parser.add_argument(
        "--max_depth",
        metavar="MAX_DEPTH",
        type=int,
        required=False,
        default=3,
        help="Max depth till where to show tree. Valid values > 0",
    )

    return parser.parse_args()


def print_error_message(msg):
    message = colored(msg, "yellow")
    print(f"{ERROR_BANNER} {message}")
    sys.exit()


def main():
    args = parse_args()

    root_dir = args.dir
    if not pathlib.Path(root_dir).is_dir():
        print_error_message("The Specified dir doesn't exists")

    max_depth = args.max_depth
    if max_depth <= 0:
        print_error_message(f"invalid value of max_depth: {max_depth}")

    DirectoryTree(TreeGenerator(root_dir, max_depth)).generate()
