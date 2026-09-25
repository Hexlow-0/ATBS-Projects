
user = {
    "name": 'jOHn sMITh',
    "email": 'John.Smith@EMAIL.COM',
    "city": 'sYDNEY',
    "membership": "PREMIUM"
    }

def clean_data():

    name = user.get('name', 'missing').title()
    email = user.get('email', 'missing').lower()
    city = user.get('city', 'missing').capitalize()
    membership = user.get('membership', 'missing').upper()

    return {'name': name,
            'email': email,
            'city': city,
            'membership': membership
            }

cleaned = clean_data()

print(f"Welcome, {cleaned['name']}!")
print(f"Email: {cleaned['email']}")
print(f"City: {cleaned['city']}")

if cleaned['membership'].isupper():
    print(f"Membership: {cleaned['membership']} - Membership is valid")
else:
    print("Membership tier needs fixing.")



