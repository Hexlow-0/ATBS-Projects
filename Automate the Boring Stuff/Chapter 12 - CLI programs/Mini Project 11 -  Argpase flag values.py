
import argparse

parser = argparse.ArgumentParser(description="String upper/reverse thingy")
parser.add_argument('-n', '--name', type=str, default='World')
parser.add_argument('-g', '--greeting', type=str, default='Hello')
parser.add_argument('-u', '--upper', action='store_true')
args = parser.parse_args()

if args.upper:
    args.greeting = args.greeting.upper()
    args.name = args.name.upper()

print(f"{args.greeting}, {args.name}!")
