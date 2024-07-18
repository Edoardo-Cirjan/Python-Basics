import random
import time

print("Hello! Welcome to your lucky number for the day finder. I am going to pick a number for you! :)")
time.sleep(0.5)
print("Picking a number....")
time.sleep(0.5)

guess = int(input("There you go.. try to find the number i picked for you! GO: "))
correct_number = random.randint(1, 9)
guess_count = 1

while guess != correct_number:
    time.sleep(0.3)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("You got it wrong :( .... please try again with a higher number! Pick another one: "))
    elif guess > 9:
        guess = int(input("You cannot pick a number greater than 9. Please pick a number between 1 & 9 :): "))
        guess_count -= 1
    else:
        guess = int(input("Not again :( .... you will have to try again with a lower number! Pick another one: "))

print(f"FINALLY! YOU GOT IT! You got your lucky number for the day: {correct_number}! It took you {guess_count} picks.")


