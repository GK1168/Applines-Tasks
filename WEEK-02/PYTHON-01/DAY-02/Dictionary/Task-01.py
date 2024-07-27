'''Convert two lists into a dictionary
        keys = ['Ten', 'Twenty', 'Thirty']
        values = [10, 20, 30]
        o/p:-{'Ten': 10, 'Twenty': 20, 'Thirty': 30}'''
        
        
key_list = list(input("Enter keys sep by comma :: ").split(','))
values_list = list(map(int,input("Enter values sep by comma :: ").split(',')))
print(f"Given ==>  keys list : {key_list} - values list : {values_list}")

dictionary = dict()
if(len(key_list) == len(values_list)):
    for i in range(len(key_list)):
        dictionary[key_list[i]] = values_list[i]
else:
    print("lists lengths are mismatched")
        
print(f"Generated dict --> {dictionary}")