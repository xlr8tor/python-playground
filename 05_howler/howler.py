#!/usr/bin/env python3

import io
import os
import sys
import argparse


#-------------------------------
def get_args():
    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


def main():
    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout

    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()


if __name__ == "__main__":
    main()