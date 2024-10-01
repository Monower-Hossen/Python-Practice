'''2. Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Tamim", "Monower", "Hossen","Sakib","Sumon","Siam"]'''

l = ["Tamim", "Monower", "Hossen","Sakib","Sumon","Siam"]

for name in l :
    if(name.startswith("S")):
        print(f"Hello sir : {name}")
