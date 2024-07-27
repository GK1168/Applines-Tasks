#Program to find whether a string is a palindrome.


string = input("Enter a string::")
temp = string
result = ''
while(temp != ''):
    char = temp[-1]
    result += char
    temp = temp[:-1]
    
print(f"Given String : {string} - Reversed String : {result}")

if (string == result):
    print(f"{string} --> Palindrome")
else:
    print(f"{string} --> Not a palindrome")