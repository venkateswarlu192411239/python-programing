arr=[0,5,4,9,3,1,7]
max=arr[0]
min=arr[0]
for num in arr:
   if num>max:
    max=num
    if num<min:
      min=num
print("maximum number:",max)
print("minimum number:",min)