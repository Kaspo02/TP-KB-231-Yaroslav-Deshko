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

def enterNum():
    try:
        a = input("a: ")
        b = input("b: ")
        return float(a), float(b)
    except ValueError:
        print("Err: Please enter valid numbers")
        raise

def enterOpr():
    try:
        opr = input("operation(+, -, *, /) or 'quit' to exit: ").strip().lower()

        valid_operations = ['+', '-', '*', '/', 'quit']

        if opr not in valid_operations:
            raise ValueError("Invalid operation")
        
        return opr
    
    except Exception as e:
        print(f"Error in entering operation: {e}")
        raise
    
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Err: Division by zero"



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