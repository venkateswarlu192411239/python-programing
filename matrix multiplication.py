a=[[1,1,1],[2,2,2],[3,3,3]]
b=[[1,1,1],[2,2,2],[3,3,3]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print(c)
for nums in c:
    print(nums)