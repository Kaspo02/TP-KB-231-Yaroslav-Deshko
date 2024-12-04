import csv
from sys import exit


def readFile(path:str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"File not found: {path}")
        answer = input("Do you want to create a new file? [y] or [n] ")
        if answer.lower() == "y":
            createCSVFile(path)
            return []
        else:
            exit(0)


def createCSVFile(path: str):
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write("")
            print(f"file {path} created")
            file.close()
    except FileExistsError:
        print(f"Error: File '{path}' exists")
    except IOError as e:
        print(f"Error: {e}")


def saveCSV(path:str, data:list):
    try:
        with open(path, "w", encoding="utf-8") as file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
            file.close()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except IOError as e:
        print(f"Error: {e}")