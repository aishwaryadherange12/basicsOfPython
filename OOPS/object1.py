class Animal:
    name='Jully'
    color= 'white'

    def bark(self):
        print("Bark Tooo Much!")

jully = Animal()
print(jully.name)
print(jully.color)

jully.bark()

class Flower:
    def __init__(self,name,color,fregrance):
        self.name = name
        self.color = color
        self.fregrance = fregrance


    def displayName(self):
        print("Name=>",self.name)

rose = Flower('rose','red',True) 
print(rose.name)       
print(rose.color,rose.fregrance)
rose.displayName()