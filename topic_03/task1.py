def calculator(opr: str):
    a, b = enterNum()
    match opr:
        case "+":
            return add(a, b)
        case "-":
            return sub(a, b)
        case "*":
            return mul(a, b)
        case "/":
            return div(a, b)
        case _:
            return "Invalid operation"
        
        
def enterNum():
    a = input("a: ")
    b = input("b: ")
    return float(a), float(b)

def enterOpr():
    opr = input("operation(+, -, *, /) or 'qiut' to exit: ")
    return opr
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
    opr = enterOpr()
    if opr!="quit":
        print(calculator(opr))
    else: 
        print("Exit")
        break
    