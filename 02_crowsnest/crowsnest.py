#!/usr/bin/env python3

"""Crow's Nest"""

import argparse
import re

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description="Crow's Nest -- choose the correct article", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar="word", help="A word")
    return parser.parse_args()

def main():
   args = get_args()
   article = 'an' if re.search(r'^[aeiou]',args.word, re.IGNORECASE) else 'a'
   print(f'Ahoy, Captain, {article} {args.word} off the larboard bow!')


if __name__ == "__main__":
    main()