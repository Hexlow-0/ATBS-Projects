
import sys

def build_output(args):

    flags = set(args)
    unknown = flags - {'-w', '-h', '-f', '-q'}
    if unknown:
        sys.exit(f"Unknown option(s): {' '.join(sorted(unknown))}\n"
                "Usage: python weather.py [-w] [-h] [-f] [-q]")

    c_temp = 22
    condition = f"Today's weather: Sunny, {c_temp}^C"

    if '-q' in flags:
        return condition
    if '-w' in flags:
        condition += "\n   💨 15 km/h winds"
    if '-h' in flags:
        condition += "\n   💧 60% humidity"
    if '-f' in flags:
        f_temp = (c_temp * 9/5) + 32
        condition = condition.replace('^C', '^F').replace(f"{c_temp}", f"{f_temp}")

    return condition

def main():

    output = build_output(sys.argv[1:])

    print(output)

if __name__ == '__main__':
    main()
