from sys import argv

from utils import *
from file_handler import readFile, saveCSV

def main():
    students = readFile(argv[1])
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X save and exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                students = addNewElement(students)
                print("New element has been added")
                printAllList(students)
            case "U" | "u":
                print("Existing element will be updated")
                students = updateElement(students)
                print("Element has been updated")
            case "D" | "d":
                print("Element will be deleted")
                students = deleteElement(students)
            case "P" | "p":
                print("List will be printed")
                printAllList(students)
            case "X" | "x":
                saveCSV(argv[1], students)
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()