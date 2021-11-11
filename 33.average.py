sum=0
a=1
while a<=11:
    b=int(input("enter the number"))
    if b%5==0:
        sum=sum+b
        avg=sum/11
    a=a+1
print(avg)