
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1


num=int(input("enter the number"))
i=1
while i<=num:
    j=0
    while j<=num-i:
        print(" ",end="")
        j=j+1
        k=1
        while k<=i:
            print("*",end="")
            k=k+i
    print()
    i=i+1

