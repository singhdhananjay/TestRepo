import pprint , os, sys, math
from math import sin, pi
nulltype=None

print(type(nulltype))
message = '''122333'''

data= lambda: 10
#print(data())

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] +=1

#pprint.pprint(count)
#comphersion
myList=[x**2 for x in range(10)]
disctionary ={x: x+1 for x in range(0, 2)}

page ="""1111112233445566"""
