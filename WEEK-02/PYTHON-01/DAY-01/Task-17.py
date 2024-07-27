#Reverse a Number using a while loop


number = int(input("Enter a number ::"))
temp = number
reverse = 0
while(number > 0):
    digit = number%10
    reverse = reverse*10+digit
    number = number//10
    
print(f"Given Number : {temp} - Reversed Number : {reverse}")