num=int(input("enter the number"))
sum=0
while num>0:
    a=num%10
    num//=10
    sum+=a
print(sum)