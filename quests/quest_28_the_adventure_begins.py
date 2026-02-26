#Defined a function called detective that which provide you with a ditective role
#Tells the user the role the have and asks them the roles they want 
#after chosing from those roles then the systen prints out what is desighned for each path 
def detective():
    print("You now have a role of a detective!")
    choice= input("discover or ignor: ")
    if choice== "discover":
        print("Your so close to the truth")
    else:
        print("You got a no clue situation! Game over")
#created a function called police
def police():
    #printed or showed the user the mission they hold apon this role
    print("Your on a mission to catch a criminal")
    #the user choses the path they take while knowing the role
    choice = input("Take the case or leave?:  ")
    #Their decisions determins the message they get depending on the word they chose 
    if choice == "Take":
        print("You're onto something, it's about to go down")
    else:
        print("Mission failed, back to square one! Game over! Goodbye")
 # This is where the impementation of those funtions happens at this main function called begin       
def begin():
    #It promps the user the challenge or the adventure begins
    print("Your adventure begins!")
    #then user choses among the roles which to take 
    choice = input("Do you want to play as a detective or the police?: ")
    #due to tha decision you make the role you desire is called to perform all it has
    if choice == "detective":
        detective()
    elif choice == "police":
        police()
    else:
        print("Invalid choice.")
        # Then we call our main function too for it to be able to execute
        
begin()
                    