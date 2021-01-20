L1=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(0,3):
    for j in range(0,3):
        if i>j:
            L1[i][j]=0


for i in range(0,3):
    for j in range(0,3):
        print(L1[i][j],end=" ")
    print()
