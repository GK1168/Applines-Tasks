'''.Create a function in Python that accepts a string and the python must return a string with each character
      in the original string doubled. If you send the “now” function as a parameter it must return “nnooww,”.
      If you send “123a!”, it must return “112233aa!!”.'''



string = input("Enter a string :: ")
new_string = ''
for i in string:
    new_string += i*2
    
print(f"Given String : {string} - Resulted String : {new_string}")