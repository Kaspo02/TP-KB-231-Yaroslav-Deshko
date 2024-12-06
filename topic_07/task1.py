class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __repr__(self):
        return f"Student name={self.name}, age={self.age}"


students = [
    Student("John", 18),
    Student("Ellie", 19),
    Student("Alex", 18),
    Student("Olivia", 19)
]

sorted_students = sorted(students, key= lambda student : student.name)

for student in sorted_students:
    print(student)

sorted_students = sorted(students, key= lambda student : student.age)
for student in sorted_students:
    print(student)