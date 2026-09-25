
cars = [
    {"make": "toyota", "year": "2015", "price": "8500", "mileage": "54000"},
    {"make": "HONDA", "year": "two thousand", "price": "12000", "mileage": None},
    {"make": "Ford", "year": "2018", "price": "free", "mileage": "89000"},
    {"make": "", "year": "2020", "price": "15000", "mileage": "32000"},
    {"make": "Mazda", "year": None, "price": "9750", "mileage": "seventy thousand"},
]

for car in cars:

    make = car.get('make')

    if not make:
        continue

    try:
        year = int(car.get('year'))
    except (ValueError, TypeError):
        year = 0

    try:
        price = int(car.get('price'))
    except (ValueError, TypeError):
        price = 0

    try:
        mileage = int(car.get('mileage'))
    except (ValueError, TypeError):
        mileage = 0

    print(f"{make.capitalize()} | Year: {year} | Price: ${price:,} | Mileage: {mileage:,}km")
