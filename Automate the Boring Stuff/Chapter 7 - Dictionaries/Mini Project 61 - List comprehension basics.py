
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = [i * 2 for i in numbers]

print(doubled)

even = [i for i in numbers if i % 2 == 0]


print(even)

even_doubled = [i * 2 for i in numbers if i % 2 == 0]

print(even_doubled)
