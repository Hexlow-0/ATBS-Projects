
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

replace = ['even' if num % 2 == 0 else 'odd' for num in numbers]

print(replace)

double_triple = [num * 2 if num % 2 == 0 else num * 3 for num in numbers]

print(double_triple)

high_or_low = ['high' if num > 5 else 'low' for num in numbers]

print(high_or_low)
