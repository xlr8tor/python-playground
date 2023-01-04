#!/usr/bin/env python3

import os
import argparse

#-------------------------------
def get_args():
    parser = argparse.ArgumentParser(description="Howler (upper-cases input)", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', help='Input string or file')

    parser.add_argument('-o', '--outfile', help='Output filename', default='')
    return parser.parse_args()

def main():
    args = get_args()
    file = args.text
    if os.path.isfile(file):
        print(open(file).read().upper())
    else:
        print(args.text.upper())





if __name__ == "__main__":
    main()