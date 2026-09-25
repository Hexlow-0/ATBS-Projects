
flights = [
    {"passenger": "  marco  ", "destination": "SYDNEY", "seat_class": "business", "bags": "2"},
    {"passenger": "Sara", "destination": "london", "seat_class": "FIRST", "bags": "three"},
    {"passenger": "  ", "destination": "TOKYO", "seat_class": "economy", "bags": "1"},
    {"passenger": "JAMES", "destination": "paris", "seat_class": "PREMIUM", "bags": None},
    {"passenger": "Priya", "destination": "", "seat_class": "economy", "bags": "2"},
]


def clean_flights(flight, errors):

    passenger = flight.get('passenger', "").strip().capitalize()

    destination = flight.get('destination', "").strip().capitalize()

    if not passenger or not destination:

        errors.append({
                    'record': flight,
                    'reason': 'Missing name or destination'
                    })

        return None

    seat_class = flight.get('seat_class').lower()

    if seat_class not in ['economy', 'business', 'first']:

        errors.append({
                    'record': flight,
                    'reason': 'Invalid seat class'
                    })

        return None

    try:
        bags = int(flight.get('bags', 0))
    except (ValueError, TypeError):
        bags = 0

    return {
            'passenger': passenger,
            'destination': destination,
            'seat_class': seat_class,
            'bags': bags
            }

def print_flights(cleaned_to_pass, errors):

    print("Valid records:\n")

    for passengers in cleaned_to_pass:

        passenger = passengers['passenger']
        destination = passengers['destination']
        seat_class = passengers['seat_class']
        bags = passengers['bags']

        print(f"{passenger} | Dst: {destination} | Class: {seat_class} | Bags: {bags}")

    print()
    print("Errors:\n")

    for error in errors:

        record = error['record']
        reason = error['reason']

        print(f"Record: {record} | Reason: {reason}")

    print()

def main():

    errors = []
    cleaned_to_pass = []

    for flight in flights:

        cleaned = clean_flights(flight, errors)

        if not cleaned:
            continue

        cleaned_to_pass.append(cleaned)

    print_flights(cleaned_to_pass, errors)

main()
