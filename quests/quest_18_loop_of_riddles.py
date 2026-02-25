#!/usr/bin/python3
success = int(input("Enter a number:"))
while success != 25:

    print(f"Ooops {success} is incorrect 😭")
    success = int(input("Enter a number:"))

print(f"You guessed {success}. The guessed number is correct! 🎉")
