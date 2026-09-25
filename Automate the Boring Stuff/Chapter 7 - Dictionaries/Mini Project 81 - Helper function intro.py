

values = ["42", "hello", None, "17", "ninety", "8", None, "5"]


def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

valid = [safe_int(v) for v in values]

print(valid)

