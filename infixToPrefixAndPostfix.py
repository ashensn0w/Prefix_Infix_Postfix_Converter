def infixToPrefixAndPostfix():
    def inf2postfix(exp):
        alph = set('abcdefghijklmnopqrstuvwxyz')
        pr1 = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []
        postfix = []

        for ch in exp:
            if ch == ' ':
                continue
            if ch in alph:
                postfix.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()

            elif ch in pr1:
                if len(stack) == 0:
                    stack.append(ch)
                elif stack[-1] != '(' and pr1[stack[-1]] >= pr1[ch]:
                    while stack and stack[-1] != '(' and pr1[stack[-1]] >= pr1[ch]:
                        postfix.append(stack.pop())
                    stack.append(ch)

                else:
                    stack.append(ch)

        while len(stack):
            postfix.append(stack.pop())

        return postfix


    def inf2prefix(exp):
        e1 = ''

        for i in range(len(exp) - 1, -1, -1):
            if exp[i] == '(':
                e1 += ')'
            elif exp[i] == ')':
                e1 += '('
            else:
                e1 += exp[i]

        rev = inf2postfix(e1)

        return rev[::-1]


    infix = input("\nEnter an Infix Expression: ")

    prefix = inf2prefix(infix)
    print("\nPrefix notation:", end=' ')
    for ch in prefix:
        print(ch, end='')
    print()

    postfix = inf2postfix(infix)
    print("Postfix notation:", end=' ')
    for ch in postfix:
        print(ch, end='')
    print()


    def anpro(exp):
        inf2postfix(exp)
        inf2prefix(exp)