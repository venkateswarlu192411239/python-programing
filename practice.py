a=145

while a>0:
    n=a%10
    f=1
    s=0
    for i in range(1,n+1):
        f=f*i
        s+=f
    print("factorial of ",n," is:",end=' ')
    print(f)
    print(s)
    a=a // 10
if s==f:
   print("strong number")
else:
    print("not perfect number")