'''2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user. '''

English = int(input("Enter Marks in English: "))
Physics = int(input("Enter Marks in Physics: "))
Chamistry = int(input("Enter Marks in Chamistry: "))

# Check for total percentage
total_percentage = (100*(English + Physics + Chamistry))/300

if(total_percentage>=40 and English>=33 and Physics>=33 and Chamistry>=33):
    print("You are passed:", total_percentage)

else:
    print("You are failed, try again next year:", total_percentage)




# marks1 = int (input("Enter Marks 1 : "))
# marks2 = int (input("Enter Marks 2 : "))
# marks3 = int (input("Enter Marks 3 : "))
#
#
# total_percentage = (marks1+marks2+marks3)/300
#
# if(total_percentage >= 40):
#     print("you are pass")
#
# else:
#     print("you are failed,try again next year!")