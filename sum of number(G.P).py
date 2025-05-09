''' 1+1/2**2+1/3**2'''
s=0
a=int(input("Enter till how many number to add"))
for i in range(1,a+1):
    s=s+1/(i**2)
print(s)
