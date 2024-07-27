#


number = int(input("Enter a number::"))
a,b = 0,1
print(a,b,end=" ")
for i in range(number-2):
    a,b=b,a+b
    print(b,end=" ")