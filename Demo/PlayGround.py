import pprint , os, sys, math, collections, threading
from math import sin, pi

#data= lambda: 10
#print(data())

class A(object):
    def foo(self,x):
        print("normal : {} {}".format(self,x))

    @classmethod
    def class_foo(cls,x):
        print("Class or construtor : {} {}".format(cls,x))

    @staticmethod
    def static_foo(x):
        print("Static: {}".format(x))  

    data= lambda x: print(x)

x= A()
x.foo(10)

A.data("lambda")
A.class_foo(20)
A.static_foo(30)

def whattheheck():
    print(whattheheck) 

whattheheck()