import re
import operator


def isNumber(token) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False

def getPrecedence(operator: str) -> int:
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    return precedence.get(operator, 0)


def infixToPostfix(expression:str) -> list:

    tokens = re.findall(r'\d+\.?\d*|[+\-*/^()]', expression.replace(' ', ''))

    output = []
    oprStack = []


    for token in tokens:
        if isNumber(token):
            output.append(token)

        elif token == "(":
            oprStack.append(token)

        elif token == ")":
            while oprStack and oprStack[-1] != "(":
                output.append(oprStack.pop())
            oprStack.pop()

        elif token in ["+", "-", "*", "/", "^"]:
            while oprStack and getPrecedence(token) <= getPrecedence(oprStack[-1]):
                output.append(oprStack.pop())
            oprStack.append(token)

    while oprStack:
        output.append(oprStack.pop())
    
    return output


def evaluatePostfix(postfixTokens:list) -> float:
    stack = []

    operators = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
        "^" : operator.pow,
    }

    for token in postfixTokens:
        if isNumber(token):
            stack.append(float(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Неправильний вираз")
            b = stack.pop()
            a = stack.pop()

            result = operators[token](a, b)
            
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Неправильний вираз")

    return stack[0]


def main():
    try:
        while True:
            expression = input("ВВедіть вираз: ")

            postfix = infixToPostfix(expression)
            s = ''
            for token in postfix:
                s = s + token + " "
        
            print(f"Postfix: [{s}]")
            
            try:
                result = evaluatePostfix(postfix)
            except ValueError as e:
                print(f"Error: {e}")

            print(result)

    except KeyboardInterrupt:
        print("Exit...")


if __name__ == "__main__":
    main()