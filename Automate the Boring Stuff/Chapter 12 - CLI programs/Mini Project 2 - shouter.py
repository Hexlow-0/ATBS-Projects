
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python shouter.py <words> <-n> (n=number)")
        sys.exit()

    arguments = sys.argv[1:]

    if '-n' not in arguments:
        for word in arguments:
            print(word.upper())
    else:
        arguments.remove('-n')

        if len(arguments) < 1:
            print("Usage: python shouter.py <words> <-n> (n=number)")
            sys.exit()

        for i, word in enumerate(arguments, start=1):
            print(f"{i}. {word.upper()}")

if __name__ == '__main__':
    main()
