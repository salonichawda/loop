a=int(input("enter the number"))
b=0
i=1
while i<=a:
    if a%i==0:
        b=b+1
    i=i+1
if b==2:
    print(a,"number is prime")
else:
    print(a,"number is not prime")




num=int(input("enter the number"))
i=1
while i<=num:
    b=0
    j=1
    while j<=num:
        if i%j==0:
            b+=1
        j+=1
    if b==2:
        print(i,"prime")
    else:
        print(i,"not prime")
    i+=1