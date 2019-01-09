class Person(): 
    print(__name__)  
    
    def __init__(self, firstName, LastName):
        self.Name= firstName
        self.Last=LastName

    def FullName(self):
        return self.Name+ self.Last
