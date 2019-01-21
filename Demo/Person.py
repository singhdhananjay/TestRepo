class Person(): 
    print(__name__)  
    
    def __init__(self, firstName, LastName):
        self.Name= firstName
        self.Last=LastName

    def FullName(self):
        return self.Name + self.Last
 
    def SomeMethod(self, required, *argss, **kwargss):
        print(required)
        if argss:
            print(argss)
        if kwargss:
            print(kwargss)   
    def toString(self):
        return '{}'.format(self.FullName())        

    SomeMethod("Hello", 1,2,3, kye1="Vl1", key2="Vl2")    


