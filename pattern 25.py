a=int(input("enter the no of rows :"))

for i in range(1,a+1):
    c=0
    for j in range(1,2*a):
        if j>=i and j<=2*a-i:
            print(chr(c+65),end="")
            c=c+1
        else:
            print(" ",end="")
    print()
