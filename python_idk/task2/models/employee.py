import models.person as p

class Employee(p.Person):
    def __init__(self, name, age, address, experience):
        super().__init__(name, age, address)
        self.experience = experience
    
    def lie(self):
        lie = self.experience * 2
        print(f"My experience is {lie}")

    def greet(self):
        print(f"Hello, I'm {self.name}, and I 100% don't smoke inside of a building")
