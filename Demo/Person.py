class Person(): 
    #print(__name__)  
    
    def __init__(self, firstName, LastName):
        self.Name= firstName
        self.Last=LastName
        print(self)

    def FullName(self):
        return self.Name + self.Last
 
    def SomeMethod(self, required, *argss, **kwargss):
        print(required)
        if argss:
            print(argss)
        if kwargss:
            print(kwargss)   
    def __str__(self):
        return '{}'.format(self.FullName())        

    #SomeMethod("Hello", 1,2,3, kye1="Vl1", key2="Vl2")    

class Worker(Person):
    def __init__(self, firstName, LastName, typeOfWork):
        super().__init__(firstName, LastName)
        self.typeOfWork = typeOfWork

    def __str__(self):
        return "{0}".format(super().__str__())    

w= Worker("D","J", "DonkeyWork")        