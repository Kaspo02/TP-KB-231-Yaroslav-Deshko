from operations import enterNum, enterOpr
from functions import add, sub, mul, div
import logging


logging.basicConfig(
    filename="topic_06/task1/log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger()

def calculator(opr: str):
    a, b = enterNum()
    logger.info(f"first number: {a}")
    logger.info(f"second number: {b}")
    match opr:
        case "+":
            return add(a, b)
        case "-":
            return sub(a, b)
        case "*":
            return mul(a, b)
        case "/":
            return div(a, b)


logger.info("Program start")
while True:
    try:
        opr = enterOpr()
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