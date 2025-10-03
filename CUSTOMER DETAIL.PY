a=input("enter name:")
b=int(input("enter mobile number:"))
c=float(input("enter cost:"))
if c>=5000:
    discount=c*0.20
elif c>=3000:
    discount=c*0.15
elif c>=2000:
    discount=c*0.10
else:
    discount=c*0.05
total=c-discount
print(a)
print(b)
print("cost:",c)
print("total:",total)
