a=int(input("enter the number"))
i=0
while i<=a:
    j=1
    while j<=i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=a-i:
        print("*",end=" ")
        k=k+1
    print()
    i=i+1
