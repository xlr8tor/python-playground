#!/usr/bin/env python3

import os
import argparse

#-------------------------------
def get_args():
    parser = argparse.ArgumentParser(description="Howler (upper-cases input)", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', help='Input string or file')

    parser.add_argument('-o', '--outfile', help='Output filename', default='', metavar='outfile')
    return parser.parse_args()

def main():
    args = get_args()
    file = args.text
    result = ''
    if os.path.isfile(file):
       result = open(file).read().upper()
    else:
        result = args.text.upper()

    if args.outfile: 
        out_fh = open(args.outfile,'wt')
        out_fh.write(result)
        out_fh.close()
    else:
        print(result)


if __name__ == "__main__":
    main()