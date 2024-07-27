#.Prompt user to enter a number and print out its factorial (using looping).


#import math
number = int(input("Enter a number::"))
#print(f"Number : {number} \nFactorial : {math.factorial(number)}")

fact = 1
for i in range(1,number+1):
    fact *= i
    
print(f"Number : {number}\nFactorial : {fact}")