import pprint , os, sys, math

nulltype=None

print(type(nulltype))
message = '''122333'''
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] +=1

#pprint.pprint(count)
#comphersion
# s=[x**2 for x in range(10)]
# print(s)

