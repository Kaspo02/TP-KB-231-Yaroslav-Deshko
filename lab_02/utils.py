def printAllList(students:list):
    for elem in students:
        print(f"Student name is {elem['name']}, phone is {elem['phone']}, email is {elem['email']} and group is {elem['group']};")


def addNewElement(students:list, newItem:dict = None):
    if newItem == None:
        name = input("Pease enter student name: ")
        phone = input("Please enter student phone: ")
        email = input("Please enter student email: ")
        group = input("Please enter student group: ")
        newItem = {"name": name, "phone": phone, "email": email, "group": group}
    else :
        name = newItem["name"]

    if students:
        insertPosition = 0
        for item in students:
            if name > item["name"]:
                insertPosition += 1
            else:
                break
        students.insert(insertPosition, newItem)
    else: 
        students = [newItem]
    return students


def deleteElement(students:list, pos:int = None):
    if not students:
        print("there are no elements in the database")
        return []
    
    if pos != None:
        del students[pos]
        return students
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
    return students


def updateElement(students: list):
    if not students:
        print("There are no elements in the database")
        return

    name = input("Please enter name to be updated: ")

    updPos = -1
    for item in students:
        if name == item["name"]:
            updPos = students.index(item)
            break

    if updPos == -1:
        print("Element was not found")
        return

    workDict = students[updPos]
    
    students = deleteElement(students, updPos)
    
    workDict["name"] = input(f"Enter new name for [{workDict['name']}]: ") or workDict["name"]
    workDict["phone"] = input(f"Enter new phone for [{workDict['phone']}]: ") or workDict["phone"]
    workDict["email"] = input(f"Enter new email for [{workDict['email']}]: ") or workDict["email"]
    workDict["group"] = input(f"Enter new group for [{workDict['group']}]: ") or workDict["group"]

    return addNewElement(students, workDict)