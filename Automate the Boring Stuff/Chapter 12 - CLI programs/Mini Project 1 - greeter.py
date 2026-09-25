
import sys

def main():

    try:
        name = sys.argv[1]
    except IndexError:
        print("No name provided - try again.")
        sys.exit()

    print(f"Hi {name}!")

if __name__ == '__main__':
    main()
