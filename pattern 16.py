a=int(input("enter the no : "))
for i in range(0,a):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,2*(a-i)-1):
        print("*",end="")
    print()
