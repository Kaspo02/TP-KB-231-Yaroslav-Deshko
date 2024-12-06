
class Operations:

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