import random
guess = 0

random_number = random.randint(1, 100)

print (" Guess The Number Game! ")

text = input (" Guess a number between 1 and 100: you have 5 guesses ")

while random_number != "text" and guess < 4:
    if text < random_number:
        print " Your guess is too low! "
        text = input (" Guess a number between 1 and 100: ")
        guess = guess + 1
    elif text > random_number:
        print " Your guess is too high! "
        text = input (" Guess a number between 1 and 100: ")
        guess = guess + 1
    else:
        print " You guessed the number! "
        break
if guess <= 4:
    print " You Lose! "
    
