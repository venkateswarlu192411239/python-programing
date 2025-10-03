def find_composite_numbers(start,end):
    composite_numbers=[]
    for num in range(start,end+1):
       if num>1:
           for i in range(2,num):
               if num%i==0:
                   composite_numbers.append(num)
                   break
    return composite_numbers
start=1
end=20
composite_numbers=find_composite_numbers(start,end)
print(composite_numbers)