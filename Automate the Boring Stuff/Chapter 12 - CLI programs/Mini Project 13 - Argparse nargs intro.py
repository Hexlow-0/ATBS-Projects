
import argparse

def add_numbers(args):

    total = 0

    for i in args:
        total += int(i)

    return total

def main():

    parser = argparse.ArgumentParser(description="Number Adder Thing")
    parser.add_argument("nums", nargs='+', type=int, help='numbers to add together')
    args = parser.parse_args()

    total = add_numbers(args.nums)

    print(f"Total: {total:,}")

if __name__ == '__main__':
    main()
