#Write a Python program to sort a given dictionary by key

key_list = list(input("Enter keys sep by comma :: ").split(','))
values_list = list(map(int,input("Enter values sep by comma :: ").split(',')))

user_dict = dict(zip(key_list,values_list))
print(user_dict)
sort = sorted(user_dict)
print(sort)
sorted_dict = {i:user_dict[i] for i in sort}
print(f"Given dict : {user_dict} ==> Sorted dict : {sorted_dict}")