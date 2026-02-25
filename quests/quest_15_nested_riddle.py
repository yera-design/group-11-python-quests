direction = input("do you go left or right? ")

if direction == "left":
    action = input("do you swim or wait? ")
    if action == "swim":
        print("you found a treasure chest!")
    else:
        print("you waited too long and fell asleep.")
else:
    print("you went right and got lost in the forest.")