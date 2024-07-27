#Program to Find Sum of Natural Numbers Using Recursion

number_input = int(input("Enter a number:: "))

def sum(number):
    if number <=0:
        return 0
    else:
        return number+sum(number-1)
    
print(f"Given Number : {number_input} --> Sum = {sum(number_input)}")