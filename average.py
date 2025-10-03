pos_sum=[]
neg_sum=[]
for i in range(1,10):
    number=int(input("enter numbers:"))


    if number>0:
        pos_sum.append(number)
        
    elif number<0:
        neg_sum.append(number)
        

if len(pos_sum)>0:
    pos_avg=sum(pos_sum)/len(pos_sum)
    print(pos_avg)
else:
    print("no positive nums")

if number<0:
    neg_avg=sum(neg_sum)/len(neg_sum)
    print(neg_avg)
else:
    print("no negative nums")


