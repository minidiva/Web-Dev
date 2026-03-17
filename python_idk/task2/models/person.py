class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        print(f"[Name: {self.name}\nAge: {self.age}\nAddress: {self.address}]")

    def greet(self):
        print(f"Hello, I'm {self.name}")
    
    def tellAge(self):
        print(f"My age: {self.age}")
