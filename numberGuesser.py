import random

top_of_range = input("Type the maximum limit or number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if(top_of_range) < 0:
        print("Enter a positive number: ")
        quit()

else:
    print("Please type a number next time.")

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guesses = input("Make a guess: ")
    user_guesses = int(user_guesses)

    if user_guesses == random_number:
        print("You got it. ")
        break
    elif user_guesses > random_number:
        print("Your guess is above the number:")
    else:
        print("Your guess is less than the number: ")

print("You got it in", guesses, "guesses. ")
