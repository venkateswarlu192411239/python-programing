num=int(input("enter number"))
s=0
for i in range(1,num):
    if num % i==0:
         s=s+i
         print(s)
if s==num:
    print("perfect number:",s)
else:
    print("Not perfect number:",s)