import random
# a computer chooses a random number between 1 and 10
secret_number= random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number:
    print("congratulations! You guessed it!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Too low!")
    