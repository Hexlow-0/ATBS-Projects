
default_settings = {
    'theme': 'light',
    'font': 'Arial',
    'font_size': 12,
    'language': 'en',
    'notifications': True,
}

user_settings = {
    'theme': 'dark',
    'font_size': 14,
    'notifications': False,
    'auto_save': True,
    'timezone': 'AEST',
}

# A
base_default_settings = set(default_settings)

# B
base_user_settings = set(user_settings)

merged = {**default_settings, **user_settings}

overridden = base_user_settings & base_default_settings

only_user = base_user_settings - base_default_settings
only_default = base_default_settings - base_user_settings

print("Overridden:")
print(overridden)
print()

print("Only user:")
print(only_user)
print()


print("Only default:")
print(only_default)
print()

for k, v in merged.items():

    print(k ,v)

