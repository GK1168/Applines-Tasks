#write a program to calculate the factorial( using Recursion)

number_input = int(input("Enter a number:: "))

def fact(number):
    if number <= 0:
        return 1
    else:
        return number*fact(number-1)
    
print(f"Given input number : {number_input} - factorial : {fact(number_input)}")