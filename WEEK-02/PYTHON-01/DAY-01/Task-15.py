#.Python Program to Display the multiplication Table

number = int(input("Enter a number::"))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")