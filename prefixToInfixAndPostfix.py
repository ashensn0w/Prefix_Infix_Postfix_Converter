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
