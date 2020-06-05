# Jose Soto
# Guessing Game Chapter 5 Program

import random

print("------------------------------")
print("       M&M guessing game!"     )
print("------------------------------")

mm_count = random.randint(1,100)
attempts_limit = 5
attempts = 0
print("Guess the number of M&Ms and you get lunch on the house!")

while attempts < attempts_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}.")
        break
    elif guess < mm_count:
        print("Sorry, that's too low!")
    else:
        print("Sorry, that's too high!")

print(f"You are done after {attempts} attempts!")
