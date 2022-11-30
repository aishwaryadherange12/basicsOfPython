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

#################################################
#  20.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 SET  IN PYTHON
# 👉 DICTIONARY  IN PYTHON
#################################################

# SET OPERATIONS mathematical


# e = {0,2,4,6,8,10}
# o = {0,1,3,5,7,9}

# o1 ={3,5}
# n1 = {'a','b'}

# # print(e.intersection(o))
# # print(e.union(o))
# # print(e.difference(o))
# # print(e.symmetric_difference(o))
# # print(o1.issubset(o))

# print(e.union(o))
# print(e.intersection(o))
# print(o.intersection(e))

# print(e.difference(o))
# print(o.difference(e))

# print(e.symmetric_difference(o))
# print(o.symmetric_difference(e))

# # boolean

# print(o1.issubset(o))
# print(n1.issubset(e))

# DICTIONARY  IN PYTHON
# word : meaning, syn, details, eg:
# discipline unique


# word : meaning
# key : value
# uinque* : anything

z  = {'name' : 'Prakash'}
print(type(z)) #<class 'dict'>

z  = {'name' : 'Prakash',
    'roll no.' : 58 , 
    'Addr' : 'Nagpur'}

print(z)

# list
# tuple

#indexing is in form of numbers  !!!
# keys are like index


# accessing  the data in a dict :

dict1 = {
    'name' : 'Viplov',
    'roll no.' : 54,
    'Addr' : 'Jalpigudi',
    'Hobby' :  'cricket',
    # [101,55,21,9] : 'Scores' unhashable type: 'list'
    # '(101,55,21,9)' : 'Score' ok... but not to be used
    'Score' :[101,55,21,9],
    1 : 'ONE'
}

print(dict1)

# discipline : good
# wrong  : good


# print(dict1['name'])
# print(dict1['Score'])
# print(dict1['roll no.'])
# print(dict1[1])

# print(dict1.keys())
# print(type(dict1.keys()))


# print(dict1.values())



# print(dict1.items())
# print("*****items*****")
# for i,j in dict1.items():
#     print(i,j)

# print("*****keys*****")
# for i in dict1.keys():
#     print(i)
# print("*****values*****")
# for i in dict1.values():
#     print(i)


# methods


dict1 = {
    'name' : 'Viplov',
    'roll no.' : 54,
    'Addr' : 'Jalpigudi',
    'Hobby' :  'cricket',
    # [101,55,21,9] : 'Scores' unhashable type: 'list'
    # '(101,55,21,9)' : 'Score' ok... but not to be used
    'Score' :[101,55,21,9],
    1 : 'ONE'
}


dict1.update({2 : 'TWO'})
print(dict1)

# deleting object

dict1.pop('Addr')
print(dict1)

#################################################
#  21.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 DICTIONARY  IN PYTHON
#################################################


'''
1 .DATA TYPES IN PYTHON
> NUMBERS
    > INT
    > FLOAT
    > COMPLEX
> BOOLEAN
>STRINGS
> LIST
> TUPLE
> SETS {}
'''

#  why dictionary ??
# user defined defined 
# faster search , faster code 
# logical mapping 
# INDEX =  0 1 2 3 4 5 6 7
# KEYS  = a , b ,c ,d ,e ,f 
# zillion, zebra , zero




dict_student = {
    'name' : 'Viplov',
    'roll no.' : 54,
    'Addr' : 'Jalpigudi',
    'Hobby' :  'cricket',
    # [101,55,21,9] : 'Scores' unhashable type: 'list'
    # '(101,55,21,9)' : 'Score' ok... but not to be used
    'Score' :[101,55,21,9],
    1 : 'ONE'
}


print(dict_student['Addr'])

#           0    1   2 
list_num = ['a','b','c']
print(list_num[2])


dict_num ={
        "NAME" : 'Alok',
        "ADDR" : 'bangalore',
        "GRADE" : 'c - grade'

}

print(dict_num['GRADE'])

# rainfall in telangala 

# creating dictionary using tuples

a = ("nirmal" , 33.33)
b = ("Nizamabad" , 55.25)
c = ("Jaynagar" , 101)

rain_data = dict([a,b,c])

print(rain_data)


print(rain_data['Nizamabad'])


# using zip functio
print("***********")

list_dist = ['nirmal','Nizamabad','Jaynagar']
list_rain = [ 33.33 ,55.25, 101]

rain_data_l = dict(zip(list_dist,list_rain))
print(rain_data_l)

rain_data_k = dict(zip(['nirmal','Nizamabad','Jaynagar'], [ 33.33 ,55.25, 101]))
print(rain_data_k)

# checking memory location of dict

print(id(rain_data))
print(id(rain_data_l))
print(id(rain_data_k))

print(rain_data ==rain_data_l == rain_data_k)



# methods


print(rain_data.get('Nizamabad'))
print(rain_data['Nizamabad'])


# print(rain_data['Hybd']) #KeyError does not exit

print(rain_data.get('Hybd')) #None
print(rain_data.get('Hybd','value does not exit for this Place')) #None
print(rain_data.get('Nizamabad','value does not exit for this Place'))
print(rain_data.get('Pune','NOt in Telangana'))


# update
rain_data['Nizamabad'] = 65.25
print(rain_data)

rain_data.update({'Nizamabad':75.25})
print(rain_data)


# rain_data['Adilabad'] = 88.23
# print(rain_data)


rain_data.update({'Adilabad':99.23})
print(rain_data)


# setdefault

dict_student = {
    'name' : 'Viplov',
    'roll no.' : 54,
    'Addr' : 'Jalpigudi',
    'Hobby' :  'cricket',
    # [101,55,21,9] : 'Scores' unhashable type: 'list'
    # '(101,55,21,9)' : 'Score' ok... but not to be used
    'Score' :[101,55,21,9],
    1 : 'ONE'
}


dict_student.setdefault('pref')
print(dict_student)


score_team = {
    'Team B' : 0,
    'Team C' : 0,
    'Team D' : 0
}

score_team.setdefault("Team A" ,5)
print(score_team)

score_team.setdefault("Team E" ,0)
print(score_team)

# is dictionary ordered or unorderd ??? Python 3.6/7 is an ordered one

#################################################
#  22.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 DICTIONARY  IN PYTHON
#################################################

'''
1 .DATA TYPES IN PYTHON
> NUMBERS
    > INT
    > FLOAT
    > COMPLEX
> BOOLEAN
>STRINGS
> LIST
> TUPLE
> SETS {}
> dictionary {}
'''


# HOW TO CREATE A DICTIONARY
a_var = dict(name = "rahul", age = 32 ,job = 'teacher')

d_tup = dict([('name',"Akash"),('age',35),('job',"Instructor")])

b_basic = {'name': 'Nikhita' , 'age': 26 , 'job' : 'SOftwareTeste'}




list_keys = [1,2,3,4,5,6]
list_values= ["one","two","three","four","five","six"]

c_zip = dict(zip(list_keys ,list_values))


# x_basic = dict('name': 'Nikhita' , 'age': 26 , 'job' : 'SOftwareTeste')

print(a_var)
print(d_tup)
print(b_basic)
# print(x_basic)
print(c_zip)


z = {}
print(type(z))

#----------------------------------------------------
#Unpacking
def allin1(a,b):
    z = a*b
    w = a+b
    y = a/b
    return z,w,y


ans  = allin1(10,50)
print(ans)
print(type(ans)) #tuple

print(ans[0])
print(ans[1])
print(ans[2])

# unpacking of tuple
ans1, ans2, ans3  = allin1(10,50)

print(ans1 , ans2 ,ans3)

# placeholder
ans1, _, _  = allin1(10,50) # not interested in ans2 and ans3

print(ans1 , _ ,_)


def func5(a):
    z = a*2
    return z


ans = func5("MINSKOLE")
print(ans)

# list/tuple as input


list_num = [1,2,3,4,5,6]

def func6(a):
    return a*2


ans = func6([1,2,3,4,5,6])
print(ans)
print(type(ans))



def double(z):
    s = []

    for i in range(len(z)):
        s.append(z[i]*2)
    return s

ans  = double([1,2,3,4,5,6])
print(ans)

ans1 = double([11,22,33,44])
print(ans1)

ans3 = double((11,22,33,44))
print(ans3)
print(type(ans3))


# returning multiple values when my i/p is list/tuple
def double(z):
    s = []

    for i in range(len(z)):
        s.append(z[i]*2)
    return s ,z 

ans1 = double([11,22,33,44])
print(ans1)
print(ans1[1]) # printin the value of z only