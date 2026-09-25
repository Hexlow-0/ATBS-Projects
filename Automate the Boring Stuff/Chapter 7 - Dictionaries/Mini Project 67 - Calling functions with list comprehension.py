
names = ['  alice  ', 'BOB', '  carol  ', 'DIANA']

def clean_name(n):

   return n.strip().title()

cleaned = [clean_name(n) for n in names]

print(cleaned)
