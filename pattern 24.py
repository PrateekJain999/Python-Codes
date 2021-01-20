a=int(input("enter the no :"))

for i in range(1,a+1):
    for j in range(1,2*a):
        if j>=a+1-i and j<a+i:
            print(i-abs(4-j),end="")
        else:
            print(" ",end="")
    print()
