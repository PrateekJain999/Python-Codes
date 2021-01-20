a=int(input("enter the rows : "))

for i in range(1,a+1):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(0,2*i-1):
        print(chr(65+k),end="")
    print()
