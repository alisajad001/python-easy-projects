print("Welcome to Human quiz game!")

is_playing = input("Do you want to play? (yes/no): ")
score = 0
if is_playing != "yes":
    quit()

print("Great! Let's start the game!")

answer = input("How many eyes do humans have? (number): ")
if answer == "2":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 2.")

answer = input("Do humans have tails? (yes/no): ")
if answer == "no":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is no.")

answer = input("What is the color of the blood in human body? (color): ")
if answer == "red":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is red.")

answer = input("Do humans have wings? (yes/no): ")
if answer == "no":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is no.")


# Result
print(f"Your score is {score}/4")
print(f"Your percentage is {int((score / 4 * 100))}%")
print("Thanks for playing!")
