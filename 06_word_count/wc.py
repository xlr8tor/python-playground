#!/usr/bin/env python3

import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("file",
                        metavar="FILE",
                        help="Input file(s)",
                        nargs="*",
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


def main():
    args = get_args()


if __name__ == "__main__":
    main()