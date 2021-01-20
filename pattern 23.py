a=int(input("enter the rows : "))

for i in range(1,a+1):
    for j in range(1,2*a+1):
        if j>=5-i and j<=3+i:
            print(abs(4-j),end="")
        else:
            print(" ",end="")
    print()
