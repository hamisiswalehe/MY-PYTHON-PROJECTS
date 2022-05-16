import random

trials = 0

number = random.randint(1, 50)

while trials < 5:
    guess = int(input("Enter the guess number:"))

    trials += 1

    if guess < number:
        print("Higher")

    elif guess > number:
        print("Lower")

    elif guess == number:
        break

if guess == number:
    trials = str(trials)
    print(f"Good job,you selected the right number in {trials} guesses!")

elif guess != number:
    number = str(number)
    print(f"Nope,the number i was thinking was {number}")


