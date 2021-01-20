a=int(input("enter the no of rows : "))

for i in range(1,a+1):
    for j in range(a-i,0,-1):
        print(" ",end="")
    for j in range(0,2*i-1):
        print(chr(2*i-1+64),end="")

    print()
