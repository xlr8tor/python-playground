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
    total_lines, total_words, total_bytes = 0, 0, 0
    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_bytes += len(line)
            num_words += len(line.split())
        total_bytes += num_bytes
        total_lines += num_lines
        total_words += num_words

    print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')


if __name__ == "__main__":
    main()