import pprint , os, sys, math, collections, threading
from math import sin, pi
class A(object):
    def __init__(self):
        print("default constructor") 

    def foo(self,x):
        print("normal : {} {}".format(self,x))

    @classmethod
    def class_foo(cls,x):
        print("Class or construtor : {} {}".format(cls,x))

    @staticmethod
    def static_foo(x):
        print("Static: {}".format(x))  

    data= lambda x: print(x)

def whattheheck():
    print(whattheheck) 


x= A()
x.foo(10)
A.class_foo(20)
A.static_foo(30)
A.data("lambda")


whattheheck()