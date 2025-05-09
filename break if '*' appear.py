c=input("Enter the key: ")
u=l=n=0
while True:
    if c=='*':
        break
    elif c.islower():
        l+=1
    elif c.isupper():
        u+=1
    elif c.isdigit():
        n+=1
print("The number of upper case are :", u)
print("The number of lower case are :", l)
print("The number are :", n)
