"""
    Group 4:
            Brigola, Jaycee T.
            Cruz, Jan Miles P.
            Jugueta, Ashley Sheine N.
            Levardo, John Race T.
            Malapit, Sthanly Paul L.
            Neptuno, Noli Y.
            Pastor, Nathalie G.
"""

import os
import colorama
from colorama import Fore, Back, Style
from infixToPrefixAndPostfix import infixToPrefixAndPostfix
from prefixToInfixAndPostfix import prefixToInfixAndPostfix
from postfixToPrefixAndInfix import postfixToPrefixAndInfix

colorama.init(autoreset = True)
choice = True

while choice:
    print("\n")
    print("=" * 50)
    print(Fore.LIGHTYELLOW_EX + Back.BLACK + "\t\t    MAIN MENU")
    print("=" * 50)
    print(Fore.CYAN + "[1] = Infix to Prefix and Postfix")
    print(Fore.GREEN + "[2] = Prefix to Infix and Postfix")
    print(Fore.BLUE + "[3] = Postfix to Prefix and Infix")
    print(Fore.RED + "[0] = Exit")

    choice = input("\n>>Please enter your choice: ")

    if choice == '1':
        print("\nYou chose: Infix to Prefix and Postfix.")
        print(Fore.GREEN + "Calling the function...")
        infixToPrefixAndPostfix()

    elif choice == '2':
        print("\nYou chose: Prefix to Infix and Postfix")
        print(Fore.GREEN + "Calling the function...")
        prefixToInfixAndPostfix()

    elif choice == '3':
        print("\nYou chose: Postfix to Prefix and Infix")
        print(Fore.GREEN + "Calling the function...")
        postfixToPrefixAndInfix()

    elif choice == '0':
        print("\nYou chose Exit.")
        print("\nThank you for using this program!")
        os._exit(0)

    else:
        print("\nInvalid input. Please try again.")
