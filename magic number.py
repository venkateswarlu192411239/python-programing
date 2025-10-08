a=1946
while a>9:
    s=0
    while a>0:
       n=a%10
       s+=n
       a=a//10   
if a<10:
    print("magic number")
else:
    print("not magic number")
