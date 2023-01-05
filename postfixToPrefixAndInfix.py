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
    userPostfix = input("\nEnter a Postfix Expression: ")

    #to call the methods for converting postfix to infix and prefix and store it in a variable
    infix = postfixToInfix(userPostfix)
    prefix = postfixToPrefix(userPostfix)

    #displays the conversion from postfix to prefix and infix notation
    print("-" * 50)
    print("\t\t      RESULT")
    print("-" * 50)
    print("Prefix notation: " + prefix + "\nInfix notation: " + infix)