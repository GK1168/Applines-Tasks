'''Display cubes of numbers using anonymous functions.
        Note: Use map with a lambda function to calculate the cube of each number'''
import math

        
number_list = list(map(int,input("Enter number sep by comma:: ").split(',')))
cube_list = list(map(lambda x:int(math.pow(x,3)),number_list))
print(f"Given list :{number_list} - cube list : {cube_list}") 