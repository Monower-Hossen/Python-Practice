'''Write a program to fill in a letter template given below with name and date.
letter =
Dear Name!
You are selected!\nIt's about both the journey and the destination!\nHave a enjoy!
Date
'''

massage = '''Dear Name! 
You are selected!\nIt's about both the journey and the destination!\nHave a enjoy!
Date '''

print(massage.replace("Name", "Tamim").replace("Date", "24 November 2030"))
