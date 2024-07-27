'''print all elements in a list
      print all even index elements in a list
      print all odd index elements in a list'''



list = list(map(int,input("Enter number list sep by comma::").split(',')))
even_index_list = [list[i] for i in range(len(list)) if i%2==0]
odd_index_list = [list[i] for i in range(len(list)) if i%2!=0]

print(f"Given List : {list}\nEven indexed List : {even_index_list}\nodd indexed list : {odd_index_list}")