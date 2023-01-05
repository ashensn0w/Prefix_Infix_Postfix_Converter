"""
    Group 4:
        Brigola, Jaycee T.
        Cruz, Jan Miles P.
        Jugueta, Ashley Sheine N.
        Levardo, John Race T.
        Malapit, Sthanly Paul L.
        Pastor, Nathalie G.
"""

import os
from infixToPrefixAndPostfix import infixToPrefixAndPostfix

choice = True
while choice:
    print("\n")
    print("=" * 50)
    print("\t\t    MAIN MENU")
    print("=" * 50)
    
    print("[1] = Infix to Prefix and Postfix")
    print("[2] = Postfix to Prefix and Infix")
    print("[3] = Prefix to Infix and Postfix")
    print("[0] = Exit")

    choice = input("\n>>Enter your choice: ")

    if choice == '1':
        print("\nYou choose: Infix to Prefix and Postfix.")
        print("Calling the function...")
        infixToPrefixAndPostfix()

    elif choice == '2':
        print("\nYou choose: Postfix to Prefix and Infix")
        print("Calling the function...")
        #postfixToPrefixAndInfix

    elif choice == '3':
        print("\nYou choose: Prefix to Infix and Postfix")
        print("Calling the function...")
        #prefixToInfixAndPostfix

    elif choice == '0':
        print("\nYou choose Exit.")
        print("\nThank you for using this program!")
        os._exit(0)

    else:
        print("\nInvalid input. Please try again.")