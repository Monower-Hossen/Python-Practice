'''6. Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A+
70 – 80 => A
60 – 70  =>A-
50 – 60 => B
40 – 50 => C
33-40 => D
<33 => F'''

marks = int(input("Enter your marks: "))

if( marks>=90):
    grade = "Ex"
elif(marks>=80):
    grade = "A+"
elif(marks>=70):
    grade = "A"
elif(marks>=60):
    grade = "A-"
elif(marks>=50):
    grade = "B"
elif (marks >= 40):
    grade = "C"
elif (marks >= 33):
    grade = "D"
elif (marks < 33):
    grade = "F"

print("Your grade is:", grade)