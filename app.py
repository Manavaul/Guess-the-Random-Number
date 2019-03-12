import random

random_number = random.randint(1, 100)

print (" Guess The Number Game! ")

text = input (" Guess a number between 1 and 100: ")

while random_number != "text":
    if text < random_number:
        print " Your guess is too low! "
        text = input (" Guess a number between 1 and 100: ")
    elif text > random_number:
        print " Your guess is too high! "
        text = input (" Guess a number between 1 and 100: ")
    else:
        print " You guessed the number! "
        break
