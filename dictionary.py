#same like object
#Dicionary not store with index
#stores values in pair like key:value or prop:value
person = {
    "fname":"aish",
    "lname":"dherange",
    "age":23
}
# print(person[2]) not work bec not store with index 
#1. retrive
print(person['fname'])#aish
# or
print(person.get('lname')) #dherange

#2. update
person['age'] = 24 
print(person['age']) # 24

#3. add
person['city'] = "sangamner"
print(person) #{'fname': 'aish', 'lname': 'dherange', 'age': 24, 'city': 'sangamner'}

# 4.delete
del person["age"]
print(person)#{'fname': 'aish', 'lname': 'dherange', 'city': 'sangamner'}

print(len(person))
print("fname" in person) #True
print("fname" not in person) #false

student = {
    "fname":"aish",
    "lname":"dherange",
    "rollNo":1,
    "fname":"aishwarya"
}
print(student)#{'fname': 'aishwarya', 'lname': 'dherange', 'rollNo': 1}
# if same key at one dictionary then last value will be print