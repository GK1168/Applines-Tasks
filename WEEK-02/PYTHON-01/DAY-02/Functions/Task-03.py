'''. Write a program that generates 4 digit permutations using digits 0-9.
        Note: Position of character IS important. Hence, both 1234 and 4321 are valid combinations.'''

'''import itertools
list1 = list(itertools.permutations(range(10),4))

def convertTuple(t):
    num = t[0]
    for i in t[1:]:
        num = num*10 + i
    return num

for i in range(len(list1)):
    list1[i] = convertTuple(list1[i])

print(list1)'''
'''list = []
for i in range(0,10000):
    if len(str(i)) == 4:
        list.append(i)
        
print(list)'''
list = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for m in range(10):
                list.append(int(str(i)+str(j)+str(k)+str(m)))

print(list)

