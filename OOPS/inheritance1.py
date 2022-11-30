#2 Parent 2 Child

class Father():
    def __init__(self,fName,fLName):
        self.fName = fName
        self.fLName= fLName
    def displayName(self):
        print('Father Method')

class Mother():
    def __init__(self,fName,fLName):
        self.fName = fName
        self.fLName= fLName
    def displayName(self):
        print('Mother method')            

class Daughter(Father,Mother):
    pass

class Son(Mother,Father):
    pass

aish = Daughter('sunil','D')
aish.displayName()

yash = Son('sunil','D')
yash.displayName()
