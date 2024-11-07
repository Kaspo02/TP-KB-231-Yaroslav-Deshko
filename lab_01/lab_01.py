
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
students = [
    {"name":"Bob", "phone":"0631234567", "email": "mail@mail.com", "group":"gr-123"},
    {"name":"Emma", "phone":"0631234567", "email": "mail@mail.com", "group":"gr-123"},
    {"name":"Jon",  "phone":"0631234567", "email": "mail@mail.com", "group":"gr-123"},
    {"name":"Zak",  "phone":"0631234567", "email": "mail@mail.com", "group":"gr-123"}
]

def printAllList():
    for elem in students:
        print(f"Student name is {elem['name']}, phone is {elem['phone']}, email is {elem['email']} and group is {elem['group']};")

def addNewElement(newItem:dict = None):
    if newItem == None:
        name = input("Pease enter student name: ")
        phone = input("Please enter student phone: ")
        email = input("Please enter student email: ")
        group = input("Please enter student group: ")
        newItem = {"name": name, "phone": phone, "email": email, "group": group}
    else :
        name = newItem["name"]

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    return

def deleteElement(pos:int = None):
    if pos != None:
        del students[pos]
        return
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del students[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    # implementation required
    updPos = -1
    for item in students:
        if name == item["name"]:
            updPos = students.index(item)
            break
    if updPos == -1:
        print("Element was not found")
    else:
        workDict = students[updPos]
        deleteElement(updPos)
    workDict["name"] = input(f"Enter new name for [{workDict["name"]}]: ")or workDict["name"]
    workDict["phone"] = input(f"Enter new name for [{workDict["phone"]}]: ")or workDict["phone"]
    workDict["email"] = input(f"Enter new name for [{workDict["email"]}]: ")or workDict["email"]
    workDict["group"] = input(f"Enter new name for [{workDict["group"] }]: ")or workDict["group"]
    addNewElement(workDict)


def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                print("New element has been added")
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                print("Element has been updated")
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")


main()