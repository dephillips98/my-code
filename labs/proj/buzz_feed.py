#!/usr/bin/env python3::
print("Welcome to the Adventure Game!")
print("You have 100 health. Make the right choices to survive.")

health = 100

print("You are in a dark cave. You see two paths ahead.")
choice = input("Do you take the left path (L) or the right path (R)? ")

if choice == "L":
    print("You encounter a hungry wolf!")
    action = input("Do you fight (F) or run (R)? ")

    if action == "F":
        print("You defeat the wolf but get injured. -20 health.")
        health -= 20
    elif action == "R":
        print("You escape from the wolf.")
    else:
        print("The wolf attacks while you hesitate. -30 health.")
        health -= 30

    if health <= 0:
        print("Your health drops to 0. Game over!")
    else:
        print("You find a potion. Do you drink it (D) or leave it (L)? ")
        potion_choice = input()
        
        if potion_choice == "D":
            print("The potion was poisonous! -50 health.")
            health -= 50
        elif potion_choice != "L":
            print("Invalid choice!")

        if health <= 0:
            print("Your health drops to 0. Game over!")
        else:
            print("Congratulations! You reach the end with", health, "health remaining.")

elif choice == "R":
    print("You discover a hidden treasure chest!")
    open_choice = input("Do you open it (O) or ignore it (I)? ")

    if open_choice == "O":
        print("The chest was trapped! -30 health.")
        health -= 30
    elif open_choice != "I":
        print("Invalid choice!")

    if health <= 0:
        print("Your health drops to 0. Game over!")
    else:
        print("Congratulations! You reach the end with", health, "health remaining.")

