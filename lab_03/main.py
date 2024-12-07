from sys import argv

from studentUtils import StudentUtils, StudentExistsError, StudentNotFoundError
from file_handler import FileHandler



def main():

    file = FileHandler(argv[1])

    utils = StudentUtils(file.readFile())


    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X save and exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                try:
                    utils.addNewStudent()
                except StudentExistsError as e:
                    print(e)
                print("New element has been added")
                utils.printAllStudents()
            case "U" | "u":
                print("Existing element will be updated")
                try:
                    utils.editStudent(input("Please enter name to be updated: "))
                except StudentNotFoundError as e:
                    print(e)
                print("Element has been updated")
            case "D" | "d":
                print("Element will be deleted")
                try:
                    utils.delStudent(input("Please enter name to be deleted: "))
                except StudentNotFoundError as e:
                    print(e)
            case "P" | "p":
                print("List will be printed")
                utils.printAllStudents()
            case "X" | "x":
                file.saveCSV(utils.students)
                print("Exit()")
                break
            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()