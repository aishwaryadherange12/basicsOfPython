#program 1
class Student:
    #properties
    name = "aishwarya"
    age = 24
    #method
    def talk(self):
        print('Talks too much(:')

aishwarya  = Student()
print(aishwarya.name) # aishwarya
print(aishwarya.age) #33
aishwarya.talk()

vaish = Student()
print(vaish.name)
print(vaish.age)
vaish.talk()

print(vaish.name)
vaish.name = "vaishnavi"
print(vaish.name)
print(vaish.age)
vaish.age = 22
print(vaish.age)

# program2

class Vehicle:
    # fields
    color = "black"
    model ="Duster"

    # methods
    def start(self):
        print('start')
    def stop(self):
        print('stop')


#Object1
nexon = Vehicle()
print(nexon.color)
print(nexon.model)
nexon.start()
nexon.stop()
nexon.color = "black"

#Object2
Tatanano = Vehicle()
print(Tatanano.color)
print(Tatanano.model)
Tatanano.start()
Tatanano.stop()






























#Human 
# Property -- age color height weight gender
# method - talk() , walk()

#Vehicle
#Property -- color modelNo
#Method start() method()

#Bank -
# accNo , IFSC code , branchName
# Method - withdrawl() deposit()