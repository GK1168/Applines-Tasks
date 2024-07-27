#Write a program to get the maximum and minimum value of dictionary

key_list = list(input("Enter keys sep by comma :: ").split(','))
values_list = list(map(int,input("Enter values sep by comma :: ").split(',')))

user_dict = dict(zip(key_list,values_list))

print(f"Given dict : {user_dict} ==> Min value : {min(user_dict.values())} - Max value : {max(user_dict.values())}")