ascii=65
i=0
while ascii<=90:
    print(chr(ascii),end=" ")
    ascii=ascii+1
    print()
    i=i+1

num=int(input("enter the number"))
ascii=65
i=0
while i<=num:
    j=1
    while j<=i:
        print("",end=" ")
        j=j+1
    while ascii<=90:
        print(chr(ascii),end=" ")
        ascii=ascii+1
    print()
    i=i+1