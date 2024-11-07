from operations import enterNum, enterOpr
from functions import add, sub, mul, div

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


while True:
    try:
        opr = enterOpr()
        if opr == "quit":
            print("Exit")
            break
            
        result = calculator(opr)
        print(result)
        
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")