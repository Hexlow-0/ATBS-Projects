

listings = [
    {"title": "  dune  ", "author": None, "genre": "SCI-FI", "price": "$*12,99", "condition": "good"},
    {"title": "1984", "author": "ORWELL", "genre": "fiction", "price": "$8", "condition": "EXCELLENT"},
    {"title": "  ", "author": "Atwood", "genre": "fiction", "price": "$*9,99", "condition": "poor"},
    {"title": "Beloved", "author": "  ", "genre": "MYSTERY", "price": "free", "condition": "good"},
    {"title": None, "author": "Kafka", "genre": "fiction", "price": "$*7,50", "condition": "GOOD"},
    {"title": "Neuromancer", "author": "GIBSON", "genre": "sci-fi", "price": "$*11,00", "condition": "WORN"},
]


def clean_listings(listing):

    title = (listing.get('title') or "").strip().capitalize()

    if not title:

        return {'ok': False,
                'record': listing,
                'field': 'title',
                'reason': 'title missing or None value'
                }

    author = (listing.get('author') or "").strip().capitalize()

    if not author:

        return {'ok': False,
                'record': listing,
                'field': 'author',
                'reason': 'author missing or None value'
                }

    genre = (listing.get('genre') or "").lower()

    if genre not in ['sci-fi', 'fiction', 'mystery']:

        return {'ok': False,
                'record': listing,
                'field': 'genre',
                'reason': 'invalid genre'
                }

    try:
        price = float((listing.get('price') or "0").replace("$", "").replace("*", "").replace(",", "."))
    except (ValueError, TypeError):
        price = 0.0

    condition = (listing.get('condition') or "").lower()

    if condition not in ['good', 'excellent', 'poor']:

        condition = 'unknown'

    return {'ok': True,
            'data': {'title': title,
                    'author': author,
                    'genre': genre,
                    'price': price,
                    'condition': condition
                    }
                }

def print_listings(cleaned, errors):

    for data in cleaned:

        title = data['title']
        author = data['author']
        price = data['price']
        genre = data['genre']
        condition = data['condition']

        print(f"{title} by {author} | Genre: {genre} | Condition: {condition} | Price: ${price}")

    print()

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        status = error['ok']
        record = error['record']
        field = error['field']
        reason = error['reason']

        print(f"Error {i}:")
        print(f"status: {status}")
        print(f"record: {record}")
        print(f"field: {field}")
        print(f"reason: {reason}\n")

def main():

    errors = []
    cleaned = []

    for listing in listings:

        result = clean_listings(listing)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_listings(cleaned, errors)

main()







