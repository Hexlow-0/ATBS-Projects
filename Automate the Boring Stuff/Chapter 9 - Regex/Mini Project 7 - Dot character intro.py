
import re

code_pattern = re.compile('b..j')

pattern_test = ['b24j',
                'f94p',
                'r12r',
                'b00j',
                '0bb0',
                'bx🫩j',
                'f&3e',
                'jj2b',
                'fv12',
                'bedj'
                ]

for test in pattern_test:

    match = code_pattern.search(test)

    if match:
        print(f"Valid: {match.group()}")
    else:
        print(f"Invalid: {test}")
