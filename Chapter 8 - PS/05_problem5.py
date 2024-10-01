'''5. Write a python function to print first n lines of the following pattern:
***
**
* - for n = 3 '''

def pattern(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Get input from the user
n = int(input("Enter the number of lines: "))

# Print the pattern using the function
pattern(n)
