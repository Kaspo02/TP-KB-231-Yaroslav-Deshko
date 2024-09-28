def calculator():
    opr = input("operation(+, -, *, /): ")
    a, b = enterNum()
    if opr == "+":
       return add(a, b)
    elif opr == "-":
       return sub(a, b)
    elif opr == "*":
       return mul(a, b)
    elif opr == "/":
       return div(a, b)
    else: return "Invalid operation"


def enterNum():
    a = input("a: ")
    b = input("b: ")
    return float(a), float(b)

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0 : return "Err: Division by zero"
    return a/b

while True:
    print(calculator())