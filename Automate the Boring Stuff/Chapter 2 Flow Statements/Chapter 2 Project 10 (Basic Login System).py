"""
Features to include:
Use if/elif/else, while, break, and continue.
Hardcode the correct username and password at the top of your file.

Give helpful feedback after each attempt:
"Incorrect username or password."
"You have X attempt(s) left."

After 3 failed attempts, show: "Account locked. Try again later." and end the program.
If login is successful, print: "Welcome, [username]!" and exit the loop.
"""

USER = 'benmanjamin'
PASS = 'treeNut99!!'

attempts = 0

while attempts < 3:
    User = input('Enter username: ')
    Pass =  input('Enter password: ')

    if User == USER and Pass == PASS:
        print("Welcome", USER +"!")
        break

    elif User != USER or Pass != PASS:
        attempts += 1
        print("Incorrect username or password")
        print("You have ", 3 - attempts ,"attempt(s) left.")
        continue

else:
    print("Account locked. Try again later.")







