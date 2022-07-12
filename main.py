import random
import time

print( "Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number..")
time.sleep(2)
guess=int(input("Waht is your guess?"))
correct_number = random.randint(1,100)

guess_count = 1

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:

        guess = int(input("Wrong answer. Go higher! What's your guess?"))
        time.sleep(2)
    else:
        guess = int(input("Wrong answer. Go a little bit lower! What's your guess?"))

print(f"Congratulations! That's the correct answer! You needed {guess_count} guess count!")