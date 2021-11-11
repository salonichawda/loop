# n=int(input("enter the number"))
i=0
k=65
while i<=8:
    print("",end=" ")
    j=1
    while j<i:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1

# i=1
# a=65
# while i<5:
#     j=1
#     while j<i:
#         j=j+1
#     k=1
#     while k<5+i:
#         print(chr(a),end=" ")
#         k=k+1
#         a=a+1
#     print()
#     i=i+1