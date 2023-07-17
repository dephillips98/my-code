#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("What is your name? ")
    if user_input != "": 
        print("Your name is ", user_input)
    else:
        print("You look like a Monty")
    user_input1 = input("What day of the week is it?").capitalize()

    if user_input1 in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print("Today is a ", user_input1)
    else:
        print("Today feels like a Monday")
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma

main()

