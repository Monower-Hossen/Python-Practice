'''10. Write a program to print multiplication table of n using for loops in reversed
order.'''

n=int(input("Enter The Number : "))

for i in range (1 , n+1):
    print(f"{n} X {11-i} = {n*(11-i)}")

