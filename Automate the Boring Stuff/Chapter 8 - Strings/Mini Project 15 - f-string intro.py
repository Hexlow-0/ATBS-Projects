
sales = [
    ("Alice Smith", 152345.5, 0.872),
    ("Bob Jones", 89720.0, 0.654),
    ("Charlie Brown", 210000.75, 0.921),
    ("Diana Prince", 43500.25, 0.432),
    ("Ed Norton", 128900.0, 0.768),
]

print("Sales Report")
print('=' * 12)

col1, col2, col3 = 20, 17, 12

print(f"Name".ljust(col1) + "Total Sales".ljust(col2) + "Conversion".ljust(col3))
print(("-" * 4).ljust(col1) + ("-" * 11).ljust(col2) + ("-" * 10).ljust(col3))

total_revenue = 0
highest_sales = 0
top_performer = ""

for name, sales, conversion in sales:

    print(f"{name}".ljust(col1) + f"${sales:,.2f}".ljust(col2) + f"{conversion:.1%}".ljust(col3))

    total_revenue += sales
    if sales > highest_sales:
        highest_sales = sales
        top_performer = name


print('=' * 12)
print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Top performer: {top_performer}")
