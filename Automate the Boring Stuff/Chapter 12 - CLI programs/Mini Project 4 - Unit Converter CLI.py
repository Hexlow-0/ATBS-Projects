import sys
import textwrap

# ===============================
# CORE INPUT VALIDATION
# ===============================

def check_arg_number(num_str, from_unit):
    """Parse and validate the number to convert."""
    try:
        num = float(num_str)
    except ValueError:
        print("Error: the number to convert must be numeric.")
        sys.exit()

    # Temperatures are the only units allowed to go below zero.
    if from_unit not in ('fa', 'ce') and num < 0:
        print("Error: Number must be greater than zero.")
        sys.exit()

    return num


def validate_conversion(args):

    valid_conversions = {
        'km': 'miles',
        'miles': 'km',
        'kg': 'lbs',
        'lbs': 'kg',
        'fa': 'ce',
        'ce': 'fa',
    }

    unit_from = args.get('from')
    unit_to = args.get('to')

    if unit_from not in valid_conversions:
        print(f"Error: '{unit_from}' is not a supported unit.")
        sys.exit()

    if unit_to not in valid_conversions.values():
        print(f"Error: '{unit_to}' is not a supported unit.")
        sys.exit()

    if unit_from == unit_to:
        print("Error: Unit conversions cannot be the same.")
        sys.exit()

    if valid_conversions[unit_from] != unit_to:
        print(f"Error: {unit_from} --> {unit_to} does not convert.")
        sys.exit()

# ===============================
# HELP FUNCTION
# ===============================

def help_function():

    print("=" * 40)
    print("UNIT CONVERTER".center(40))
    print("=" * 40)
    print()

    help_text = """
    Usage: python converter.py <num> --from <unit1> --to <unit2>

    <num>:
    <num> = number. This is the number you want to convert, the amount/measurement.
    It can be a float. If you are converting a temperature, the number can be below
    zero. Otherwise, the number must be above zero (will error otherwise).

    <--from>:
    One of two required flags. Self explanatory; you are converting *from* one unit to
    another. If you are converting from km to miles, you must ensure "km" is the next
    argument, otherwise you'll be converting from *miles* to km.

    <unit 1/2>:
    This program supports the following units:

    - km --> miles
    - miles --> km
    - kg --> lbs
    - lbs --> kg
    - fahrenheit --> celsius
    - celsius --> fahrenheit

    The short handles for each are: km, miles, kg, lbs, fa, ce

    The program will error if two units do not make sense as a pair (can't convert miles to
    celsius, kg -> kg is pointless, etc).

    <--to>:
    The second required flag - this precedes the unit you are converting *to*. If you are
    converting miles to km, ensure the following argument is km, not miles.

    --from and --to can appear in either order, e.g. both of these work:

    - python converter.py 100 --from km --to miles
    - python converter.py 100 --to miles --from km

    Examples:

    - python converter.py 100 --from km --to miles
    - python converter.py 30.6 --from ce --to fa
    - python converter.py 180 --from lbs --to kg
    - python converter.py 8.5 --from miles --to km

    The program will error on lines like:

    - python converter.py -40 --from km --to miles (negative number, non temperature units)
    - python converter.py 30 -from ce -to fa (incorrect flag syntax)
    - python converter.py 180 --from km --to kg (invalid conversion)

    ...and so on.
    """

    print(textwrap.dedent(help_text))

    sys.exit()

# ===============================
# CALL VALIDATION LOGIC
# ===============================

def parse_args():

    args_stored = sys.argv[:]

    if len(args_stored) < 2:
        print("Usage: python converter.py <num> --from <unit1> --to <unit2>")
        print("OR: python converter.py --help")
        sys.exit()

    if args_stored[1].lower() == '--help':
        help_function()

    if '--from' not in args_stored or '--to' not in args_stored:
        print("Error: both --from and --to flags are required.")
        sys.exit()

    from_index = args_stored.index('--from')
    to_index = args_stored.index('--to')

    try:
        convert_from = args_stored[from_index + 1].lower().strip()
        convert_to = args_stored[to_index + 1].lower().strip()
    except IndexError:
        print("Error: --from and --to each require a unit after them.")
        sys.exit()

    num = check_arg_number(args_stored[1], convert_from)

    args = {'num': num, 'from': convert_from, 'to': convert_to}

    validate_conversion(args)

    return args

# ===============================
# UNIT CONVERSION FUNCTIONS
# ===============================

def convert_km_or_miles(num, unit1, unit2):

    if unit1 == 'km':
        result = num * 0.621371
    else:
        result = num * 1.60934

    return result

def convert_kg_or_lbs(num, unit1, unit2):

    if unit1 == 'kg':
        result = num * 2.20462
    else:
        result = num * 0.45359237

    return result

def convert_ce_or_fa(num, unit1, unit2):

    if unit1 == 'ce':
        result = (num * 1.8) + 32
    else:
        result = (num - 32) * 5 / 9

    return result

# ===============================
# CALL UNIT CONVERSION FUNCTIONS
# ===============================

def convert(args):

    num = args.get('num')
    unit1 = args.get('from')
    unit2 = args.get('to')

    if unit1 == 'km' or unit1 == 'miles':
        result = convert_km_or_miles(num, unit1, unit2)
    elif unit1 == 'kg' or unit1 == 'lbs':
        result = convert_kg_or_lbs(num, unit1, unit2)
    else:
        result = convert_ce_or_fa(num, unit1, unit2)

    return result

# ===============================
# PRINT RESULTS
# ===============================

def print_result(result, args):

    num = args.get('num')
    unit1 = args.get('from')
    unit2 = args.get('to')

    print(f"{num} {unit1} = {result:,.2f} {unit2}")

# ===============================
# MAIN FUNCTION POWERS PROGRAM
# ===============================

def main():

    args = parse_args()
    result = convert(args)
    print_result(result, args)


if __name__ == '__main__':
    main()
