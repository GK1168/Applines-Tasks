#.Write a Python program to iterate over dictionaries using for loops

key_list = list(input("Enter keys sep by comma :: ").split(','))
values_list = list(map(int,input("Enter values sep by comma :: ").split(',')))

dict1 = dict(zip(key_list,values_list))
print(dict1)
for i,j in dict1.items():
    print(f"{i} - {j}")