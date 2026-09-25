
coordinates = [(1, 5), (3, 2), (7, 4), (2, 8), (5, 1)]

result = [f"x:{x}, y:{y}" for x, y in coordinates]

print(result)

x_greater_than_y = [f"x:{x}, y:{y}" for x, y in coordinates if x > y]

print(x_greater_than_y)
