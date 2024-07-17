import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100! :)")
time.sleep(1)

print("Picking a number...")
time.sleep(1)

guess = int(input("What is your guess?: "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong... You need to guess higher! Pick another number!: "))
    else:
        guess = int(input("Wrong... You need to guess lower! Pick another number!: "))


print(f'YAY! You got the right answer: {correct_number}! :) It took you {guess_count} guesses.')
