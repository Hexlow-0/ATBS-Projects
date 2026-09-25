

import re

postcode = re.compile('\d{4}')
three_and_six = re.compile('[a-zA-Z]{3,6}')

postcode_test = ['1524',
                '05821',
                '1038',
                '15510',
                '2615',
                '1524',
                '2550',
                '@r13',
                '+3011',
                '8008135'
                ]

three_six_test = ['three',
                'six',
                'not_three',
                'notSIX',
                'is_six_',
                'test1',
                '4n24r',
                'thrée'
                ]

for code in postcode_test:

    match = postcode.search(code)

    if match:
        print(f"Valid code: {match.group()}")
    else:
        print(f"'{code}' not valid")

print()

for string in three_six_test:

    match = three_and_six.search(string)

    if match:
        print(f"Between 3 & 6: {match.group()}")
    else:
        print(f"'{string}' not between three at six")

print()
