"""
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function
should be able to work with any list value passed to it. Be sure to test
the case where an empty list [] is passed to your function.
"""

list = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list):
    result = ''
    for item in range(len(list)):
        if item == len(list) - 1:
            result += 'and ' + list[item]
        else:
            result += list[item] + ', '
        return result

def main():
    while True:
        play = input("You wanna see the magic (y/n)? \n")

        if play.lower() == 'y':
            print(comma_code(list))
        elif play.lower() == 'n':
            print("k.")
            break
        else:
            print("Please enter 'y' or 'n', nothing else.")
            continue

main()