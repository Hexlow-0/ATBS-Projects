
import sys
import argparse

parser = argparse.ArgumentParser(description='BMI calculator.')
parser.add_argument('weight', type=float)
parser.add_argument('height', type=float)
args = parser.parse_args()

bmi = args.weight / (args.height ** 2)
print(f"BMI: {bmi:,.1f}")


