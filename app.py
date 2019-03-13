import random

print (" Guess The Number Game! ")

random_number = random.randint(1, 100)
guess = 0
countdown = 9

text = input (" Guess a number between 1 and 100: ")

while random_number != text and guess < 9:
    if text < random_number:
        print "Your guess is too low!"
        print ('You have {} guess[es] left'.format(countdown))
        text = input (" Guess a number between 1 and 100: ")
        guess += 1
        countdown -= 1
    elif text > random_number:
        print " Your guess is too high!"
        print ('You have {} guess[es] left'.format(countdown))
        text = input (" Guess a number between 1 and 100: ")
        guess += 1
        countdown -= 1
    elif guess <= 9 and text == random_number:
        print " You guessed the number! "

if guess <= 9 and text == random_number:
    print " You guessed the number! "
elif guess == 9 and text != random_number:
    print " You Lose! "
    print "The random number was:"
    print random_number
