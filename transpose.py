L1=[[1,2,3],[4,5,6],[7,8,9]]
swap=0
for i in range(0,3):
    for j in range(0,3):
        if i<j or i==j:
            swap=L1[i][j]
            L1[i][j]=L1[j][i]
            L1[j][i]=swap


print(L1)
