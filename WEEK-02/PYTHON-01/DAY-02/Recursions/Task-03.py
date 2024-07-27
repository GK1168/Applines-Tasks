#Write a program to generate fibonacci series(using Recursion)

number_input = int(input("Enterr no.of terms u want :: "))

def fib(number):
    if number<=1:
        return number
    else:
        return fib(number-1)+fib(number-2)
    
for i in range(number_input):
    print(fib(i),end=' ')