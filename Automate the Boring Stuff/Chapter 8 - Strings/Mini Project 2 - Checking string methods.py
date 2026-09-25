
data = {
    "first_name": "John2",
    "last_name": "Smith",
    "age": "28",
    "member_id": "JohnSmith28",
    "referral_code": "   "
}

def validate_data():

    f_name = data.get('first_name', 'unknown').isalpha()
    l_name = data.get('last_name', 'unknown').isalpha()
    age = data.get('age', 'unknown').isdigit()
    member_id = data.get('member_id', 'unknown').isalnum()
    referral_code = data.get('referral_code').isspace() # if you add .strip() before .isspace() - to becomes an empty string and says its false

    return {'f_name': f_name,
            'l_name': l_name,
            'age': age,
            'member_id': member_id,
            'referral_code': referral_code
            }

validated = validate_data()

if validated.values() == True:
    print('Form submitted successfully\n')
else:
    print('Form has errors, please review\n')


print('See data:\n')

for k, v in validated.items():

    print(f"{k}: {v}")





