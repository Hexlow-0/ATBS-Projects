"""
Requirements:

Ask the user:
Their favorite color
A word they’d use to describe themselves
Their favorite animal

Create a function called generate_pet_name() that takes these three inputs as arguments and returns a custom pet name string like:
"Your pet name is: BlueFierceTiger!"

Create another function called run_pet_namer() that:
Handles the inputs
Calls generate_pet_name() with the answers

Prints the result

Add a loop so the user can generate multiple pet names until they type 'q' to quit.
"""

# Takes the users input as arguments and knits them into a name
def generate_pet_name(col, wor, ani):
    print(f"Your pet name is: {col} {wor} {ani}")

# Handles user inputs
def run_pet_namer():
    print("Welcome to the Pet Name Generator!\n")

    print("Answer the questions to generate the name of enter 'q' at anytime to quit")

    colour = input("What is your favorite color: ")
    if colour.lower() == "q":
        print("Thanks for playing!")
        exit()
    word = input("What word would you use to describe yourself: ")
    if word.lower() == "q":
        print("Thanks for playing!")
        exit()
    animal = input("What is your favorite animal: ")
    if animal.lower() == "q":
        print("Thanks for playing!")
        exit()

    # Calls name generator and passes arguments
    pet_name = generate_pet_name(colour, word, animal)
    print(pet_name)

# Sends the execution to the top of the pet namer function
while True:
    run_pet_namer()
