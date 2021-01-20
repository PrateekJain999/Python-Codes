a=int(input("enter column :"))

for i in range(a-1,-(a),-1):
    for j in range(a-1,abs(i)-1,-1):
        print(j,end="")

    print()
