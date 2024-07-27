'''Write a program that generates combinations of all lengths possible using characters from below list.
        ['a', 'b', 'c', 'd', 'e']
        Note: Position of character is NOT important. Hence, there cannot be two combinations including the same characters
        just differing in the position of characters.'''

import itertools

        
list = list(input("Enter chars sep by comma:: ").split(','))
sub = []

for i in range(len(list)+1):
    sub.extend(itertools.combinations(list,i))
print(sub)
for i in sub:
    i = ''.join(i)
    print(i)
        
 