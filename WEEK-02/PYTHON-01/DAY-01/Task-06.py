#For a given list, generate a list containing squares of even items in list


list = list(map(int,input("Enter list of numbers sep by comma::").split(',')))
new_list = [i*i for i in list]
print(f"Given list : {list}\n Squared list : {new_list}")
