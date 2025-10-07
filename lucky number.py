num=1412
digits=[int(d) for d in str(num)]
sum_digits=sum(digits)
product=1
for d in digits:
  product*=d
print(sum_digits)
print(product)
a=sum_digits
b=product
if a==b:
  print("lucky number",num)
else:
  print("not lucky number",num)