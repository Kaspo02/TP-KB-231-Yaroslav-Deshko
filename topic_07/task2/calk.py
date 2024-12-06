from operations import Operations
from functions import Calc
import logging


calc = Calc

operations = Operations

logging.basicConfig(
    filename="topic_07/task2/log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger()

def calculator(opr: str):
    a, b = operations.enterNum()
    logger.info(f"first number: {a}")
    logger.info(f"second number: {b}")
    match opr:
        case "+":
            return calc.add(a, b)
        case "-":
            return calc.sub(a, b)
        case "*":
            return calc.mul(a, b)
        case "/":
            return calc.div(a, b)


logger.info("Program start")
while True:
    try:
        opr = operations.enterOpr()
        logger.info(f"operation: {opr}")
        if opr == "quit":
            print("Exit")
            logger.info(f"the program has stopped")
            break
            
        result = calculator(opr)
        print(result)
        logger.info(f"calculation result: {result}")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        logger.info(f"the program has stopped")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logger.error(f"An unexpected error occurred: {e}")