num=int(input("enter the number"))
product=1
while num>0:
    a=num%10
    num//=10
    product*=a
print(product)