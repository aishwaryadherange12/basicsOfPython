# //same like object
animals = {
    "eye": 2,
    "legs": 4,
    "ear": 2
    }
# loop
for key in animals:
    print(key,animals[key]) #eye 2 legs 4 ear 2

# keys
print(  animals.keys()) #dict_keys(['eye', 'legs', 'ear'])
# values
print(animals.values()) #dict_values([2, 4, 2])
# items
print(animals.items()) #dict_items([('eye', 2), ('legs', 4), ('ear', 2)])

for x in animals.keys():
    print(x) #eye legs ear
for x in animals.values():
    print(x) #2 4 2
for x in animals.items(): #Keys and Values Stores in Tuple
    print(x) #('eye', 2) ('legs', 4)('ear', 2)
# unpack tuple
for x,y in animals.items():
    print(x,y)
# eye 2
# legs 4
# ear 2
    