from time import time

def MyTimer(functionToWrap):
    def f(x, y=10):
        start= time()
        returnValue = functionToWrap(x,y)
        end= time()
        print("time taken: " , end-start)
        return returnValue
    return f


@MyTimer
def add(x, y=10):
    print(x+y)

print( add(10, 20))
print(add("My name is ", "Dhananjay"))