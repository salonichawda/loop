num=int(input("enter the number"))
a=num
sum=0
i=1
while i<num:
   if num%i==0:
       sum=sum+i
   i=i+1
if sum==a:
    print(num,"is perfact number")
else:
    print(num,"is not perfact number")




i=1
while i<=30:
    j=1
    sum=0
    while j<i:
        if i%j==0:
            sum=sum+j
        j+=1
    if sum==i:
       print(i,"is perfact number")
    else:
       print(i,"is not perfact")
    i+=1   
