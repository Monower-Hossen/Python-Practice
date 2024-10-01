class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


hossen = Employee()
hossen.language = "JavaScript" # This is an instance attribute
print(hossen.language, hossen.salary)
 