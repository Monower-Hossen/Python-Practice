'''7. Write a program to find out whether a given post is talking about “Monower” or not.'''

post = input("Enter the post: ")



if("Monower".lower() in post.lower()):
    print("This post is talking about monower ")

else:
    print("This post is not talking about monower ")