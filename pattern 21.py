a=int(input("enter the no of rows : "))

for i in range(1,a+1):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(2*i-1,0,-1):
        print(k,end="")
    print()
