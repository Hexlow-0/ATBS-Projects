import random

# Define the function that returns either "heads" or "tails"
def flip_coin():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

# Start an infinite loop
while True:
    guess = input("Heads or Tails? (or type q to quit): ").lower()

    if guess == "q":
        print("Goodbye!")
        break

    if guess not in ["heads", "tails"]:
        print("Invalid input. Please type 'heads', 'tails', or 'q'.")
        continue

    result = flip_coin()  # CALL the function and save its result

    if guess == result:
        print("Correct!")
    else:
        print("Incorrect! The answer was", result)
