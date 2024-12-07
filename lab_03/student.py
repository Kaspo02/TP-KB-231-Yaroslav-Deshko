class Student:
    def __init__(self, name, phone, email, group) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group
    
    def __repr__(self) -> str:
        return f"Student name is {self.name}, phone is {self.phone}, email is {self.email} and group is {self.group};"
    
    def doDict(self):
        return {
            "name" : self.name,
            "phone" : self.phone,
            "email" : self.email,
            "group" : self.group
        }