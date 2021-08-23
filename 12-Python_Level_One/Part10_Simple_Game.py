###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

digits = list(range(10))
random.shuffle(digits)
#print(digits[:3])


def validator(guess):
    if len(guess) != 3:
        return False
    for char in guess:
        if char not in '0123456789':
            return False
    return True

# Another hint:
keep_playing = 1
while keep_playing:
    guess = input("What is your guess? ")
    if not validator(guess):
        print('The entered number is not valid')
        continue
    correct_guess = 0
    mismatched_guess = 0

    for idx, char in enumerate(guess):
        if digits[idx] == int(char):
            correct_guess += 1
        elif int(char) in digits[:3]:
            mismatched_guess += 1
    if correct_guess == 3:
        print('You got it!')
        keep_playing = 0
        continue
    if correct_guess:
        print(f"Match: You've guessed {correct_guess} correct number(s) in the correct position")
    elif mismatched_guess:
        print(f"Close: You've guessed {mismatched_guess} correct number(s) but in the wrong position")
    else:
        print("Nope: You haven't guess any of the numbers correctly")

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
