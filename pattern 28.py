a=int(input("enter column :"))

for i in range(a-1,-(a),-1):
    for j in range(abs(i),a):
        print(j,end="")

    print()
