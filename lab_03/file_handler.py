import csv
from sys import exit

from student import Student


class FileHandler:
    def __init__(self, path:str):
        self.path = path


    def readFile(self) -> list[Student]:
        data = []
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                     data.append(Student(name= row["name"], phone=row["phone"], email= row["email"], group=row["group"]))
                return data
        except FileNotFoundError:
            print(f"File not found: {self.path}")
            answer = input("Do you want to create a new file? [y] or [n] ")
            if answer.lower() == "y":
                self.__createCSVFile()
                return []
            else:
                exit(0)


    def __createCSVFile(self):
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                fieldnames = ["name", "phone", "email", "group"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader() 
                print(f"File '{self.path}' has been created.")
        except IOError as e:
            print(f"Error: {e}")


    def saveCSV(self, data: list[Student]):
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                fieldnames = ["name", "phone" ,"email", "group"]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()

                rows = [student.doDict() for student in data]
                writer.writerows(rows)

        except FileNotFoundError:
            print(f"File not found: {self.path}")
        except IOError as e:
            print(f"Error: {e}")
