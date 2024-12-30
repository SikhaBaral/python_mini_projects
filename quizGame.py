print(" -------- Welcome To The Quiz Game-------- ")

playingOption = input("Do you want to play? ")

if playingOption.lower() != "y":
    quit()

print("Okay! Let's Play")
score = 0
questions = 0

answers = input("What is the full form of CPU? ")
questions += 1
if answers.lower() == "central processing unit":
    print("CORRECT!")
    score += 1
else:
    print("IN-CORRECT!")

answers = input("What is the full form of GPU? ")
questions += 1
if answers.lower() == "graphics processing unit":
    print("CORRECT!")
    score += 1
else:
    print("IN-CORRECT!")

answers = input("What is the full form of MU? ")
questions += 1
if answers.lower() == "memory unit":
    print("CORRECT!")
    score += 1
else:
    print("IN-CORRECT!")

answers = input("What is the full form of ALU? ")
questions += 1
if answers.lower() == "arithmatic logic unit":
    print("CORRECT!")
    score += 1
else:
    print("IN-CORRECT!")

answers = input("What is the full form of CU? ")
questions += 1
if answers.lower() == "control unit":
    print("CORRECT!")
    score += 1
else:
    print("IN-CORRECT!")

result = score * 100 / questions

print("You got ", score, "answers correct.")
print("You scored ", result, "%.")