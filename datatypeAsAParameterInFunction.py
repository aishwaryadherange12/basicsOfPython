# dictionary 
# tuple 
# list 
# set 
# number as a parameter and number as return type 
r1 = 10
r2 = 5
def Addition(x,y):
    #x = r1 # separate memory
    #y = r2 # separate memory
    return x + y
sum = Addition(r1,r2)
print(sum)#15

# passing list as param

cities = ["sangamner","mumbai","nagpur","kolkalta"]
def AddCity(listC):
    # listC = cities # reference added to same memory
    listC.append("nasik")
    print(listC) #['sangamner', 'mumbai', 'nagpur', 'kolkalta', 'nasik']
AddCity(cities)
print(cities) #['sangamner', 'mumbai', 'nagpur', 'kolkalta', 'nasik']

#----------------------------------------------
# passing dict as param
# city ---- sangamner
info = {
    'firstName':"aishwarya",
    'lastName':"dherange",
    'age':24,
}

def addCity(dictInfo):
    # dictInfo = info
    dictInfo['city'] = "sangamner"
    print(dictInfo) # {'firstName': 'aishwarya', 'lastName': 'dherange', 'age': 24, 'city': 'sangamner'}
addCity(info)
print(info) # {'firstName': 'aishwarya', 'lastName': 'dherange', 'age': 24, 'city': 'sangamner'}

# passing function as parameter to another funtion
# function class function
def sum(x,y):
    return x + y
def addition(fn):
    #fn = sum
    # def fn(x,y):
    #     return x+ y

    q9 = fn()
    print(q9)#140
    print("AD")
print(sum)
# print(sum(1,3)) # printing function reference
# sum(12,3) # call function
