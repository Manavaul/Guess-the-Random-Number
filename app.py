import random
guess = 0

random_number = random.randint(1, 100)
print random_number
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
        break
if guess == 4 and text != random_number:
    print " You Lose! "
    print "The random number was:"
    print random_number
elif guess >== 4 and text == random_number:
    print " You guessed the number! "
