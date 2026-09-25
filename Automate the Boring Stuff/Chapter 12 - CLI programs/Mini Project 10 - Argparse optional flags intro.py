
import argparse

parser = argparse.ArgumentParser(description="String upper/reverse thingy")
parser.add_argument('string', type=str)
parser.add_argument('-u', '--upper', action='store_true')
parser.add_argument('-r', '--reverse', action='store_true')
args = parser.parse_args()

if args.upper:
    args.string = args.string.upper()
if args.reverse:
    args.string = args.string[::-1]

print(args.string)
