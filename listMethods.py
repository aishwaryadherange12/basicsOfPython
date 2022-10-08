#List 
#         0        1       2     3
names = ["aish","vaish","patu","yashu"]
numbers = [11,22,33,44,55,66]
mixedList = ["aish","dherange",1111111]
print(names)#['aish', 'vaish', 'patu', 'yashu']

# List stores the value by index
print(names[0]) # aish

# How to length of List ?
q1 = len(numbers)
print(q1) # 6

#max()
q2  = max(numbers)
print(q2) #66

#min()
q3 = min(numbers)
print(q3) #11

#     0  1  2   3  4  5
k = [11,22,33,44,55,66]
print(k[1]) #22
print(k[len(k)-1]) #(k[6-1]) => k[5] => 66
# length -1 is always last index

#          0        1         2       3
fruits = ["apple","mango","banana","grapes"]
for x in range(4):
  #print(x) print index i.e 0 to 3
  print(fruits[x])

listA = [22,33,44]
listB = [55,66,77]

listA.extend(listB)
print(listA)
listB.extend(listA)
print(listB)

listC = [23,33,44,55,44,66,88,44]
a3 = listC.count(44)
print(a3)

listE = ["rahul","ajay","sameer", "rohit"]
listE.sort()
print(listE)

listE.reverse()
print(listE)

listE.clear()
print(listE)