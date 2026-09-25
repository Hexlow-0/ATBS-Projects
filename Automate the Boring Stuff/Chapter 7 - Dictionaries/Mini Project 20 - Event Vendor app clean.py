
vendors = [
    {"company": "  acme ltd  ", "category": "FOOD", "stand_size": "large", "daily_fee": "$*250,00", "days_requested": "3"},
    {"company": "BobCo", "category": "retail", "stand_size": "MASSIVE", "daily_fee": "$180", "days_requested": "five"},
    {"company": None, "category": "food", "stand_size": "small", "daily_fee": "$*90,00", "days_requested": "2"},
    {"company": "  ", "category": "DRINKS", "stand_size": "medium", "daily_fee": "$*150,00", "days_requested": None},
    {"company": "Delta Inc", "category": "entertainment", "stand_size": "large", "daily_fee": "free", "days_requested": "4"},
    {"company": "Eve Events", "category": "FOOD", "stand_size": "SMALL", "daily_fee": "$*200,00", "days_requested": "2"},
    {"company": "FoodCo", "category": None, "stand_size": "medium", "daily_fee": "$*175,00", "days_requested": "3"},
]



def clean_vendor(ven):

    company = (ven.get('company') or "").strip().title()

    if not company:

        return {'ok': False,
                'record': ven,
                'field': 'company',
                'reason': 'missing company'
                }

    category = (ven.get('category') or "").strip().lower()

    if not category:

        return {'ok': False,
                'record': ven,
                'field': 'category',
                'reason': 'missing category'
                }

    if category not in ['food', 'drinks', 'retail', 'entertainment']:

        return {'ok': False,
                'record': ven,
                'field': 'category',
                'reason': 'invalid category'
                }

    stand_size = (ven.get('stand_size') or "medium").strip().lower()

    if stand_size not in ['small', 'medium', 'large']:

        stand_size = 'medium (patched)' # Adding 'patched' so i know this value needed patching

    try:
        daily_fee = float((ven.get('daily_fee') or "0").replace("$", "").replace("*", "").replace(",", "."))
    except (ValueError, TypeError):
        daily_fee = 0.0

    try:
        days_requested = int((ven.get('days_requested') or 1))
    except (ValueError, TypeError):
        days_requested = 1

    return {'ok': True,
            'data': {'company': company,
                    'category': category,
                    'stand_size': stand_size,
                    'daily_fee': daily_fee,
                    'days_requested': days_requested
                    }
                }

def print_vendor(cleaned, errors):

    print("Valid records:\n")

    for vendor in cleaned:

        company = vendor['company']
        category = vendor['category']
        stand_size = vendor['stand_size']
        daily_fee = vendor['daily_fee']
        days_requested = vendor['days_requested']

        print(f"{company}:")
        print(f"  Category: {category} | Stand size: {stand_size} | Daily fee: ${daily_fee} | Days requested: {days_requested}")


    print()

    print("Errors:\n")

    for i, error in enumerate(errors):

        print(f"Error {i}:")
        print(f"Reason: {error['reason']}")
        print(f"Field: {error['field']}")
        print(f"Record: {error['record']}\n")


def main():

    errors = []
    cleaned = []

    for ven in vendors:

        result = clean_vendor(ven)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_vendor(cleaned, errors)

main()


