#Python program to check if the number is an Armstrong number or not


import math

number = int(input("Enter a number :: "))
temp = number
length = len(str(number))
result = 0
while(temp > 0):
    digit = temp % 10
    result += math.pow(digit,length)
    temp = temp//10
    
print(f"Given Number : {number}\nSum of digits : {result}")
if(result == number):
    print(f"{number} --> Armstrong Number")
else:
    print(f"{number} --> Not an armstrong number")