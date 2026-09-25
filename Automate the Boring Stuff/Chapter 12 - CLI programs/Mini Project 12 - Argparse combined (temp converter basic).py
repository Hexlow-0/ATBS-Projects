
import argparse

def convert_temps(num, unit):

    if unit == 'kel':
        return num + 273.15
    elif unit == 'fah':
        return (num * 9/5) + 32
    else:
        return '' # just for now ig idk

def main():

    lookup = {'fah': 'fahrenheit', 'kel': 'kelvin', 'cel': 'celsius'} # bc y not, just to see if i remembered how to do it

    parser = argparse.ArgumentParser(description="Temperature converter")
    parser.add_argument('num', type=float)
    parser.add_argument('--unit', type=str, choices=['cel', 'fah', 'kel'], default='cel')
    args = parser.parse_args()

    result = convert_temps(args.num, args.unit)

    print(f"{result:.2f}° {lookup.get(args.unit, '')}")

if __name__ == '__main__':
    main()
