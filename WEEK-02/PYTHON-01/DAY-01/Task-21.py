#Program to Shuffle Deck of Cards (itertools, random)


import itertools
import random

list = list(itertools.product(range(1,10),['Spades','Clubs', 'Hearts','Diamond']))

types=['Spades','Clubs', 'Hearts','Diamond']
extend = ['King','Queen','Joker','Ace']

for i in types:
    for j in extend:
        list.append((j,i))
    
print(f"List before shuffled : \n{list}")

random.shuffle(list)
print(f"List after shuffled : \n{list}")

cards = int(input("Enter no.of cards u want to pick::"))
for i in range(cards):
    print(f"{list[i][0]} from {list[i][1]} is picked!")