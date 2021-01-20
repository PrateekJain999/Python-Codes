a=eval(input("enter the no to find the reverse of a no : "))
rev=0
while a>0:
    r=a%10
    rev=r+10*rev
    a=a//10

print("reverse of a no is : ",rev)
