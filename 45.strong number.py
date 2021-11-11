a=int(input("enter the number"))
c=a
fac=1
sum=0
i = 0
while a>0:
    b=a%10
    fac=fac*b
    sum+=fac
    a//=10
    a=a-1
    # i+=1
if c==sum:
    print("strong number")
else:
    print("not strong number")