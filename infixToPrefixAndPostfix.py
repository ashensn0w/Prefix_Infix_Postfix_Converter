def infixToPrefixAndPostfix():
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
            infix = input("\nEnter an Infix Expression: ")
            operators = ["+", "-", "*", "/", "^"]
            if infix.startswith(tuple(operators)):
                print("This is already in prefix notation")
            elif infix.endswith(tuple(operators)):
                print("This is already in postfix notation")
            else:
                prefix = inf2prefix(infix)  # Gets the prefix notation using inf2prefix () function
                print("\nPrefix notation:", end=' ')
                for ch in prefix:
                    print(ch, end='')
                print()

                postfix = inf2postfix(infix)  # Gets the prefix notation using inf2prefix () function
                print("Postfix notation:", end=' ')
                for ch in postfix:
                    print(ch, end='')
                print()
                break
            break

    Con1()  # calls main function
