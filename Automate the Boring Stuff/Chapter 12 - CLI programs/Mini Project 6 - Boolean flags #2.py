
import sys

def build_output(args):

    flags = set(args)
    unknown = flags - {'-r', '-e', '-o', '-q'}
    if unknown:
        sys.exit(f"Unknown option(s): {' '.join(sorted(unknown))}\n"
                "Usage: python counter.py [-r] [-e] (or [-o]) [-q]")

    count = [i for i in range(1, 11)]

    if '-e' in flags and '-o' in flags:
        sys.exit("Error: Can't use both even and odd flags. Try again.")

    if '-r' in flags:
        output = count.reverse()
    if '-e' in flags:
        output = [i for i in count if i % 2 == 0]
    if '-o' in flags:
        output = [i for i in count if i % 2 != 0]

    if '-q' in flags:

        for i in output:
            print(i, end=' ')
        sys.exit()
    else:
        return output

def main():

    output = build_output(sys.argv[1:])

    for i in output:
        print(i)


if __name__ == '__main__':
    main()
