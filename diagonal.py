L1=[[1,2,3],[1,2,3],[1,2,3]]

for i in range(0,3):
    for j in range(0,3):
       if i==j:
           print(L1[i][j],end=" ")
       else :
            L1[i][j]=0
            print(L1[i][j],end=" ")
    print()
