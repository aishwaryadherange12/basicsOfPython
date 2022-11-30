emp={
    "fname":"aish",
    "lname":"d",
    "age":24
}
print(emp['fname'])
print(emp.get('lname'))


# # typecasting 

# print(list(set_one))


# #accessing elements using a for loop


# for i in set_one:
#     print(i)

# # tricky questions

# z1 = (33)
# z2 = ('33')
# z3 = ("Mumbai")

# print(type(z1))
# print(type(z2))
# print(type(z3))

# print("***********")
# s1 = {12,23,45,87}
# s2 = {1}
# s3 = {"Minskole"}
# s4 = {} #<class 'dict'>


# print(type(s1))
# print(type(s2))
# print(type(s3))
# print(type(s4))


# methods
# operations on set 
# mathematical 
print("***********")

s = {44,55,66,55,66,'weak','order',False,True}
print(s)

# add 
s.add(77) # will add 77 in the set collection
print(s)

s.add(9999)
print(s)

s.add(True) # we can not add duplicate values
print(s)


# remove
s.remove(False)
print(s)



# sorted # retuen type is LIST
# print(sorted(s)) # instances of 'str' and 'int

s2 = {11,88,44,55,77,33,55,55}
print(sorted(s2))


#clear
s.clear()
print(s)

print(type(s))
print("***********")
x = set() #explicitly definig a set 
print(x)

print("***********")
y  = {}
print('ok')
print(type(y))


# del

# del(s)
# print(s)

s3 = {11,22,33}
print(list(s3)) #constructor

a = ["A", 44 ,False, True]
a.clear()
print(a)

b = {11,22,44,77}
b.clear()
print(b)


# constructor for creating/defining a set

p = set([True,False,22,22])
print(p)


r = set((True,False,22,22))
print(r)

z = set() # empty set
print(z)


d = list()  #empty list
print(d)