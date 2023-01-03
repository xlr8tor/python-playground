#!/usr/bin/env python3
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Jump the Five", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', help='Input text', metavar='str')

    return parser.parse_args()

def main():
    args = get_args()

    jumper= {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    for char in args.text:
        print(jumper.get(char,char), end='')
    print()




if __name__ == '__main__':
    main()
