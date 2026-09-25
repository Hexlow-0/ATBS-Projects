
names = ['  alice  ', 'BOB', 'carol', '  DIANA  ', 'eve']

cleaned = [name.strip().title() for name in names]

print(cleaned)

cleaned_plus_four = [name.strip().title() for name in names if len(name.strip()) > 4]

print(cleaned_plus_four)



