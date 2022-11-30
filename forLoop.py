cities = ["sangamner","pune","nasik","nagpur","kolhapur"]
#simple
for item in cities:
 print (item) 

#range(startPos,EndPos) not include last number

#print 0 to 9 number
for i in range(10):
    print(i)  #0, 1 , ... , 9

#print 5 to 8 number
for i1 in range(5,9):
    print(i1)  

for x in range(2,22,2):
  print(x) #2 , 4 , 6 ... 20

 #print Cities
for i2 in range(5):
    print(cities[i2])  

# as it is 
q7 = cities[::]
print(q7) #["sangamner","pune","nasik","nagpur","kolhapur"]

#              0      1        2       3
fruits = ["apple","banana","kiwi","grapes"]
# print all element of list

for item in fruits:
  print (item)

#              0        1           2            3
countries = ["india","pakistan","uk","srilanka"]
for x in range(len(countries)):
  print(countries[x])

#           0      1       2
names = ["aish","vaish","patu"]
print(names)
print(type(names)) #class list


info = ["aish","dherange",9920726080]
print(info) #['aish','dherange',9921726080]


marks = [11,22,33,44,55]
print(marks) #[11,22,33,44,55]

# len is property
a1 = len(marks)
print(a1) #5