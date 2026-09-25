
bookings = [
    {"guest": "  alice  ", "room_type": "SUITE", "nights": "3", "price_per_night": "$*120"},
    {"guest": "BOB", "room_type": "single", "nights": "seven", "price_per_night": "$85"},
    {"guest": "  ", "room_type": "DOUBLE", "nights": "2", "price_per_night": "$*95"},
    {"guest": "DIANA", "room_type": "penthouse", "nights": "4", "price_per_night": "$*200"},
    {"guest": "Eve", "room_type": "double", "nights": None, "price_per_night": "$110"},
]

def clean_booking(booking, errors):

    guest = booking.get('guest').strip().capitalize()

    if not guest:

        errors.append({
                'record': booking,
                'reason': 'missing guest'
                })

        return None

    room_type = booking.get('room_type').lower()

    if room_type not in ['single', 'double', 'suite']:

        errors.append({
                'record': booking,
                'reason': 'invalid room type'
                })

        return None

    try:
        nights = int(booking.get('nights', 1)) or 1
    except (ValueError, TypeError):
        nights = 1

    try:
        price = int(booking.get('price_per_night', 0).replace("$", "").replace("*", ""))
    except (ValueError, TypeError):
        price = 0

    return {'guest': guest,
            'room_type': room_type,
            'nights': nights,
            'price': price
            }


def print_bookings(clean_bookings, errors):

    print("Valid Bookings:\n")

    for bookings in clean_bookings:

        guest = bookings['guest']
        room_type = bookings['room_type']
        nights = bookings['nights']
        price = bookings['price']

        print(f"{guest} | Room: {room_type} | Nights: {nights} | Price: ${price}")

    print()

    print("Errors:\n")

    for error in errors:

        print(f"Record: {error['record']} - Error: {error['reason']}")

def main():

    clean_bookings = []
    errors = []


    for booking in bookings:

        cleaned = clean_booking(booking, errors)

        if cleaned is None:
            continue

        clean_bookings.append(cleaned)

    print_bookings(clean_bookings, errors)

main()
