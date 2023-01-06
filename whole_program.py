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
import colorama
from colorama import Fore, Back, Style

def infixToPrefixAndPostfix():
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset = True)

    def Con1():
        oprtr = {'+', '-', '*', '/', '(', ')', '^'}
        pr1 = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # level of priority for operators

        def inf2postfix(exp):
            stack = []
            postfix = []  # serves as postfix list

            for ch in exp:
                if ch not in oprtr:
                    postfix.append(ch)  # appends in postfix list
                elif ch == '(':
                    stack.append(ch)  # appends in stack
                elif ch == ')':
                    while stack[-1] != '(':
                        postfix.append(stack.pop())  # if the last element on stack is ), appends the character to postfix
                        # list
                    stack.pop()  # pops the current stack if between ()

                elif ch in pr1:
                    if len(stack) == 0:  # if the stack is empty, character is appended to stack
                        stack.append(ch)
                    elif stack[-1] != '(' and pr1[stack[-1]] >= pr1[ch]:  # as long as the last character on stack is not (
                        while stack and stack[-1] != '(' and pr1[stack[-1]] >= pr1[ch]:  # and if preceding character on
                            postfix.append(stack.pop())  # stack is >= to the last character, the preceding character
                        stack.append(ch)  # is popped to the postfix list & succeeding character is appended on stack

                    else:
                        stack.append(ch)

            while len(stack):  # appends remaining characters on stack to postfix list
                postfix.append(stack.pop())

            return postfix

        def inf2prefix(exp):
            e1 = ''  # initialization of empty string for prefix notation

            for i in range(len(exp) - 1, -1, -1):  # iteration over the characters in reverse order
                if exp[i] == '(':
                    e1 += ')'  # appends closing parenthesis if character is (
                elif exp[i] == ')':
                    e1 += '('  # appends opening parenthesis if character is )
                else:
                    e1 += exp[i]  # otherwise appends character to e1

            rev = inf2postfix(e1)  # initializes variable to call function inf2postfix() with e1 as argument

            return rev[::-1]  # returns a reversed version of inf2postfix(e1)

        while True:
            infix = input(Fore.LIGHTGREEN_EX + "\nPlease enter an infix expression: ")
            operators = ["+", "-", "*", "/", "^"]

            if infix.startswith(tuple(operators)):
                print(Fore.LIGHTRED_EX + Back.WHITE + "This is already in prefix notation")

            elif infix.endswith(tuple(operators)):
                print(Fore.LIGHTRED_EX + Back.WHITE + "This is already in postfix notation")

            else:
                prefix = inf2prefix(infix)  # Gets the prefix notation using inf2prefix () function
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Prefix notation:", end=' ')
                for ch in prefix:
                    print(ch, end='')
                print()

                postfix = inf2postfix(infix)  # Gets the prefix notation using inf2prefix () function
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Postfix notation:", end=' ')
                for ch in postfix:
                    print(ch, end='')
                print()
                break
            break
    Con1()  # calls main function

def prefixToInfixAndPostfix():
    # Prefix to infix expression conversion function
    def PrefixtoInfix(expression):
        # Generate a stack that will hold operators
        stack = []

        # Iterate through the expression in reverse order
        for ch in expression[::-1]:
            # If the character is an operand, add it to the stack
            if ch not in ['+', '-', '*', '/']:
                stack.append(ch)
            else:
                # Pop two operands off the stack if the character is an operator.
                operand1 = stack.pop()
                operand2 = stack.pop()

                # Create a new string with the operands and the operator, and add it to the stack
                new_string = '(' + operand1 + ch + operand2 + ')'
                stack.append(new_string)

        # The final expression will be the only element in the stack
        infix_expression = stack.pop()

        return infix_expression

    # Prefix to infix expression conversion function
    def PrefixtoPostfix(expression):
        # Generate a stack that will hold operators
        stack = []

        # Iterate through the expression in reverse order
        for ch in expression[::-1]:
            # If the character is an operand, add it to the stack
            if ch not in ['+', '-', '*', '/']:
                stack.append(ch)
            else:
                # If the character is an operator, pop two operands from the stack
                operand1 = stack.pop()
                operand2 = stack.pop()
                # Create a new string with the operands and the operator, and add it to the stack
                new_string = operand1 + operand2 + ch
                stack.append(new_string)

        # The final expression will be the only element in the stack
        postfix_expression = stack.pop()

        return postfix_expression

    # input and output
    expression = input("\nPlease enter a prefix expresssion: ")
    print("-" * 50)
    print("\t\t      RESULT")
    print("-" * 50)
    print('Infix notation:', PrefixtoInfix(expression))
    print('Postfix notation:', PrefixtoPostfix(expression))

#method to convert postfix to prefix and infix
def postfixToPrefixAndInfix():
    #stack class implementation to bundle data and functionality
    class Stack():
        #method that allows the class to initialize the attributes of a class
        def __init__(self):
            self.size = 0
            self.content = list()

        #method to check if stack is empty
        def is_empty(self):
            return not bool(self.content)

        #method to put new data in a stack
        def push(self, data):
            self.content.append(data)
            self.size = len(self.content) - 1

        #method to access and remove data from a stack
        def pop_(self):
            if not self.is_empty():
                data = self.content.pop()
                size = len(self.content) - 1
                return data
            else:
                return None

        #method to get the top data element of a stack without removing it
        def peek(self):
            if not self.is_empty():
                return self.content[-1]
            else:
                return None

        #method to display the data of a stack
        def display(self):
            if not self.is_empty():
                return self.content
            else:
                return None

    #method to convert a postfix to infix
    def postfixToInfix(postfix):
        #stores the "Stack()" class to "stack" variable
        stack = Stack()

        #main process
        for i in postfix:
            #condition to check if the token is an operand (alphabet or numeral)
            if i.isalpha() or i.isnumeric():
                #token will be pushed if it's true
                stack.push(i)
            
            #condition to check if the token is an operator
            elif i in ['+','-','*','/','^']:

                #popping the top two elements from the stack
                operand1 = stack.pop_()
                operand2 = stack.pop_()

                #infix operation arrangement
                result = '(' + operand2 + i + operand1 + ')'

                #result will be pushed
                stack.push(result)

            #displays content of stack   
            stack.display()

        #popped data (final)        
        return stack.pop_()

    #method to convert a postfix to prefix
    def postfixToPrefix(postfix):
        #stores the "Stack()" class to "stack" variable
        stack = Stack()

        #main process
        for i in postfix:
            #condition to check if the token is an operand (alphabet or numeral)
            if i.isalpha() or i.isnumeric():
                #token will be pushed if it's true
                stack.push(i)

            #condition to check if the token is an operator
            elif i in ['+','-','*','/','^']:

                #popping the top two elements from the stack
                operand1 = stack.pop_()
                operand2 = stack.pop_()

                #prefix operation arrangement
                result = '(' + i + operand2 + operand1 + ')'

                #result will be pushed
                stack.push(result)

            #displays content of stack
            stack.display()

        #popped data (final)
        return stack.pop_()

    #to get user input (postfix expression)
    userPostfix = input("\nPlease enter a postfix expression: ")

    #to call the methods for converting postfix to infix and prefix and store it in a variable
    infix = postfixToInfix(userPostfix)
    prefix = postfixToPrefix(userPostfix)

    #displays the conversion from postfix to prefix and infix notation
    print("-" * 50)
    print("\t\t      RESULT")
    print("-" * 50)
    print("Prefix notation: " + prefix + "\nInfix notation: " + infix)

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
