import pprint, collections
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, itemKey):
    numBrought = 0
    for nameKey in guests:
        numBrought+= int(guests[nameKey].get(itemKey,0))
      
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

#####################


d= {'a1':'a', 'b2':'b', 'c3':'c'}
for k,v in d.items():
    print(k, '-->',v)

myList= ["Dhananjay", "dhananjay", "Dhananjay", "singh"]
d2={}
for name in myList:
    key= len(name)
    d.setdefault(key, []).append(name)

while d2:
    k, v= d2.popitem()
    print(k, '-->', v)    

d3= collections.ChainMap(d, d2)
print(d3)
