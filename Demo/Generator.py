import time
# myList=[x**2 for x in range(10)]
# disctionary ={x: x+1 for x in range(0, 2)}
# print(myList)

def First():
    print("First")

def Second():
    print("Second")

def Third():
    print("Third")

def Gen():
    First()
    yield
    Second()
    yield
    Third()

# for x in Gen():
#     pass

# var=Gen()
# next(var)
# next(var)
# next(var, None)


def compute():
    for i in range(10):
        time.sleep(.5)
        yield i

# for x in compute():
#     print(x)        


