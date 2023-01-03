#!/usr/bin/env python3

import argparse

def get_args():
    """Command-line arguments"""

    parser = argparse.ArgumentParser(description='Picnic game', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("food", metavar="food", help="List food for picnic", nargs='+')

    parser.add_argument('-s', '--sorted', action='store_true', help='sort picnic list', default=False)

    return parser.parse_args()

def format_output(list, length):
    if len(list) == 1:
        return f'{list[0]}'
    if len(list) == 2:
        conjunction = ', and ' if length > 2 else ' and '
        return f'{list[0]}{conjunction}{list[1]}'
    
    return list[0] + ', ' + format_output(list[1:], length)

def main():
    args = get_args()
    food_list = args.food
   
    if args.sorted:
        food_list.sort()
    print(f'You are bringing {format_output(food_list, len(food_list))}.')

if __name__ == "__main__":
    main()