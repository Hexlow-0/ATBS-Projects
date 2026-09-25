
import sys

def build_output(args):

    flags = set(args)
    unknown = flags - {'-u', '-t', '-r', '-n'}
    if unknown:
        sys.exit(f"Unknown option(s): {' '.join(sorted(unknown))}\n"
                "Usage: python formatter.py [-u] [-t] [-r] [-n]")

    sentence = "the quick brown fox jumps over the lazy dog"

    sentence = sentence.split()

    if '-u' in flags and '-t' in flags:
        sys.exit("Error: Cannot use [-u] and [-t] options in same argument")

    if '-u' in flags:
        sentence = [i.upper() for i in sentence]
    if '-t' in flags:
        sentence = [i.title() for i in sentence]
    if '-r' in flags:
        sentence.reverse()
    if '-n' in flags:
        sentence.append(f"({len(sentence)} words)")

    return sentence

def main():

    output = build_output(sys.argv[1:])

    print(' '.join(output))

if __name__ == '__main__':
    main()
