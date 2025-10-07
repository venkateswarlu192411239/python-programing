a=[[1,1,1],[2,2,2],[3,3,3]]
b=[[1,1,1],[2,2,2],[3,3,3]]
c=[[0,0,0],[0,0,0],[0,0,0]]
d=[[2,2,2],[3,3,3],[4,4,4]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]*b[i][j]*d[i][j]
print("matrix multiplication is:")
for r in c:
    print(r)