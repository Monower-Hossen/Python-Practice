# import re
# test = "The rain in Spain"
# a = re.findall("[a-m]" , test)
#
# print(a)


import re
text = "1 is the special characters"
pattern = "^1"

a = re.findall(pattern,text)
if a :
    print("yes, 1 is special characters")
else:
    print("Nope , 1 is not special characters ")
