#Prepare a list of tuples by pairing each element from second list with element from first list.


import itertools

tuple1 = tuple(input("Enter tuple1 values sep by comma :: ").split(','))
tuple2 = tuple(input("Enter tuple2 values sep by comma :: ").split(','))
print(tuple2)
list =list(itertools.product(tuple1,tuple2))
print(list)