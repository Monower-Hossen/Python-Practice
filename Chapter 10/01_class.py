class Employee: 
    language = "Py" # This is a class attribute
    salary = 2400000

monower = Employee()
monower.name = "monower" # This is an instance attribute
print(monower.name, monower.language, monower.salary)

rohan = Employee()
rohan.name = "Tasmia Tahmid "
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class