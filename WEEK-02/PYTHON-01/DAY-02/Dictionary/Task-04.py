#Write a Python program to sum all the items in a dictionary

key_list = list(input("Enter keys sep by comma :: ").split(','))
values_list = list(map(int,input("Enter values sep by comma :: ").split(',')))

user_dict = dict(zip(key_list,values_list))
print(user_dict)
sum = 0
for j in user_dict.values():
    sum+=j
    
sum1 =user_dict.values()
print(sum1)


print(f"Given dict : {user_dict} --> Sum : {sum}")