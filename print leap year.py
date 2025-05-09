display all the leap years from 1900,2101
s=1900
e=2101
for i in range(s,e+1):
    if i%4==0:
        print(i,end=" ") 
