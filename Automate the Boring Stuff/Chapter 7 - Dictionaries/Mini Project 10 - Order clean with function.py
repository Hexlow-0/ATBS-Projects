
orders = [
    {"customer": "  marco  ", "dish": "PASTA", "quantity": "2", "price_per_item": "$12,50"},
    {"customer": "Sara", "dish": "burger", "quantity": "three", "price_per_item": "$8.99"},
    {"customer": "  ", "dish": "PIZZA", "quantity": "1", "price_per_item": "$*11.50"},
    {"customer": "JAMES", "dish": None, "quantity": "2", "price_per_item": "$15.00"},
    {"customer": "Priya", "dish": "sushi", "quantity": "4", "price_per_item": "$*13,75"},
]

def clean_order(order):

    customer = order.get('customer', "").strip().capitalize()


    dish = order.get('dish')

    if not customer or not dish:
        return None

    dish = dish.capitalize()

    try:
        quantity = int(order.get('quantity', 1))
    except (ValueError, TypeError):
        quantity = 1

    try:
        price_per_item = float(order.get('price_per_item', 0.0).replace("$", "").replace("*", "").replace(",", "."))
    except (ValueError, TypeError):
        price_per_item = 0.0

    return {
            'customer': customer,
            'dish': dish,
            'quantity': quantity,
            'price_per_item': price_per_item
            }

def main():

    for order in orders:

        cleaned_data = clean_order(order)

        if cleaned_data is None:

            continue

        customer = cleaned_data['customer']
        dish = cleaned_data['dish']
        quantity = cleaned_data['quantity']
        price = cleaned_data['price_per_item']

        print(f"{customer} | Dish: {dish} | Qty: {quantity} | Price: ${price}")

main()
