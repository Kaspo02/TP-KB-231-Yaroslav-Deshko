from student import Student


class StudentUtils:
    def __init__(self, students:list[Student]) -> None:
        self.students = students


    def printAllStudents(self):
        for student in self.students:
            print(student)

    
    def addNewStudent(self, student: Student = None):
        if student is None:
            student = self.__getData()

        if self.__isExists(student.name) != -1:
            raise StudentExistsError(student.name)

        self.students.append(student)
        self.__sort()


    def delStudent(self, name:str):
        position = self.__isExists(name)
        if  position == -1:
            raise StudentNotFoundError(name)
        del self.students[position]


    def editStudent(self, name:str):
        position = self.__isExists(name)
        if  position == -1:
            raise StudentNotFoundError(name)
        
        self.students[position] = self.__getData(self.students[position])
        self.__sort()


    def __isExists(self, name: str) -> int:
        for index, student in enumerate(self.students):
            if student.name == name:
                return index
        return -1


    def __sort(self):
        self.students = sorted(self.students, key = lambda student: student.name)


    def __getData(self, student:Student = None)-> Student:
        if student is None:
            name = input("Pease enter student name: ")
            phone = input("Please enter student phone: ")
            email = input("Please enter student email: ")
            group = input("Please enter student group: ")

            return Student(name = name, phone = phone, email = email, group = group)

        else:
            student.name = input(f"Pease enter student name [{student.name}]: ") or student.name
            student.phone = input(f"Pease enter student phone [{student.phone}]: ") or student.phone
            student.email = input(f"Pease enter student email [{student.email}]: ") or student.email
            student.group = input(f"Pease enter student group [{student.group}]: ") or student.group

            return student


class StudentExistsError(Exception):
    def __init__(self, element):
        self.element = element
        super().__init__(f'Student "{element}" already exists')


class StudentNotFoundError(Exception):
    def __init__(self, name):
        super().__init__(f'Student "{name}" not found.')