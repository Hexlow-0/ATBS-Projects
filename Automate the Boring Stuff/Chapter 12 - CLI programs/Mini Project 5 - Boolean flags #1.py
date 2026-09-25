
import sys
import datetime

def build_message(args):

    flags = set(sys.argv[1:])
    unknown = flags - {'-t', '-c', '-q'}
    if unknown:
        sys.exit(f"Unknown option(s): {' '.join(sorted(unknown))}\n"
                "Usage: python status.py [-t] [-c] [-q]")

    msg = "ok"

    if '-q' in flags:
        print(msg)
        sys.exit()
    if '-c' in flags:
        msg = msg.upper() + ' ✓'
    if '-t' in flags:
        msg += f' [{datetime.date.today()}]'

    return msg


def print_result(result):

    print(f"System status: {result}")

def main():

    result = (build_message(sys.argv[1:]))
    print_result(result)

if __name__ == '__main__':
    main()






