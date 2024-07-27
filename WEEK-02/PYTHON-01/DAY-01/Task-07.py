#For a given list, generate a list containing squares of the items in list that are greater than 10 and less than 50



list = list(map(int,input("Enter list of numbers sep by comma::").split(',')))
new_list = [i*i for i in list]
filtered_list = [i for i in new_list if i>10 and i<50]

print(f"Given list : {list}\n Squared list : {new_list}\nFiltered list : {filtered_list}")

