sum=0
num=int(input("enter the number"))
a=num
c=int(input("enter the number"))
while num>0:
    b=num%10
    i=b**c
    num//=10
    sum=sum+i
if sum==a:
    print(a,"armstrong")
else:
    print(a,"not armstrong")