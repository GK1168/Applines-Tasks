'''
.Merge two Python dictionaries into one
        dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
        dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
        o/p:{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}'''
        
        
key_list1 = list(input("Enter keys sep by comma :: ").split(','))
values_list1 = list(map(int,input("Enter values sep by comma :: ").split(',')))

dict1 = dict(zip(key_list1,values_list1))

key_list2 = list(input("Enter keys sep by comma :: ").split(','))
values_list2 = list(map(int,input("Enter values sep by comma :: ").split(',')))

dict2 = dict(zip(key_list2,values_list2))
print(f"Given ==> first dict : {dict1} - second dict : {dict2}")

print(dict1.update(dict2))
print(type(dict1),type(dict2))
def updatedDict(dict1,dict2):
    for i in dict2:
        dict1[i] = dict2[i]
    return dict1

updated_dict = updatedDict(dict1,dict2)
print(f"updated dict :{updated_dict}")