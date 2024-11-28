workList = [
    {"name": "Sam", "mark": 3},
    {"name": "John", "mark": 9},
    {"name": "Bob", "mark": 12},
    {"name": "Alex", "mark": 10},
    {"name": "Anna", "mark": 2},
    {"name": "Zack", "mark": 8},
    {"name": "Ellie", "mark": 11},
    {"name": "Olivia", "mark": 6},
]

def fprint(key: str, List:list ,reverse=False):
    sortedList = sorted(List, key= lambda x:x[key], reverse=reverse)
    for student in sortedList:
        print(f"Ім'я: {student['name']}, Оцінка: {student['mark']}")


print("За ім'ям")
fprint("name", workList)


print("За оцінкою")
fprint("mark", workList, reverse=True)
