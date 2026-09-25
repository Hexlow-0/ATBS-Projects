
base_config = {'theme': 'light', 'font': 'Arial', 'size': 12, 'language': 'en'}
user_config = {'theme': 'dark', 'size': 14, 'notifications': True}


base_keys = set(base_config.keys())
user_keys = set(user_config.keys())

overridden = base_keys & user_keys

untouched = base_keys - user_keys

added = user_keys - base_keys

merged = {**base_config, **user_config}

for k, v in merged.items():

    print(k, v)

print()

print("Overridden:\n")

for item in overridden:

    print(item)

print()

print("Untouched:\n")

for item in untouched:

    print(item)
