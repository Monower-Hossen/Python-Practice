'''4. Write a program to find whether a given number is prime ornot. '''

n = int (input ("Enter the number : "))

for i in range (2 , n ):
    if(n%i == 0 ):
        print ("number is not prime.")
        break
    else:
        print("Number is a prime.")
