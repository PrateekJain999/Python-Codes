a=int(input("enter the column :"))

for i in range(a-1,-a,-1):
    for j in range(1,abs(i)+1):
        print(" ",end="")
    for k in range(a-1,abs(i)-1,-1):
        print("*",end="")
    print()
