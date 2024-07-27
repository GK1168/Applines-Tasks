#Prompt the user for a decimal number,Convert decimal to binary and display the result


###error --> solved

'''user_input = int(input("Enter a decimal number :: "))
print(f"Given number : {user_input} - Binary number : {bin(user_input)}")'''
user_input = float(input("Enter a decimal number"))
#print(user_input)
list = [int(user_input),user_input - int(user_input)]
#print(list)
binary_values = []
for i in range(len(list)):
    if i == 0:
        binary_values.append(bin(list[i])[2:])
    else:
        res =''
        for j in range(3):
            val = list[i] *2 
            res += str(int(val))
            list[i] = val - int(val)
        binary_values.append(res)
binary_value = '.'.join(binary_values)
print(f"Given input ::{user_input} -- Binary Value : {binary_value}")