from time import time

def MyTimer(functionToWrap):
    def f(*args, **kwargs):
        start= time()
        returnValue = functionToWrap(*args, **kwargs)
        end= time()
        print("time taken: " , end-start)
        return returnValue
    return f  
    
@MyTimer
def add(x, y=10):
    return x+y
    
@MyTimer
def sub(x, y):
    return x-y

print(add(10, 20))
print(add("My name is ", "Dhananjay"))
print(sub(10, 20))