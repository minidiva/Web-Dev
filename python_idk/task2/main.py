import models.person as p
import models.boss as b
import models.employee as e


def main():
    person = p.Person("Alice", 30, "123 Main St")
    person.greet()
    person.tellAge()
    person.__str__()
    
    boss = b.Boss("Bob", 45, "456 Oak Ave", "TechCorp")
    boss.greet()
    boss.tellAge()
    boss.__str__()
    boss.rule()

    employee = e.Employee("Alex", 23, "E-11", 2)
    employee.greet()
    employee.tellAge()
    employee.__str__()
    employee.lie()

    phonebook = [person, boss, employee]

    for i in phonebook:
        print(i.name)

if __name__ == "__main__":
    main()