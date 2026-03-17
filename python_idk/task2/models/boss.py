import models.person as p

class Boss(p.Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def rule(self):
        print(f"I rule: {self.company}")

    def greet(self):
        print(f"Hello, I'm {self.name}. I am your boss")