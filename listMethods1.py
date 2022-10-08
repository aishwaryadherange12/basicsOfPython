#          0        1         2       3
fruits = ["apple","mango","banana","grapes"]
for x in range(len(fruits)):
    #print(x)
    print(fruits[x])#apple mango banana grapes

#1-index() Find index of item in list 
print(fruits.index("banana")) #2

#2-append() Add item in list at last
fruits.append("papaya")
print(fruits) #['apple', 'mango', 'banana', 'grapes', 'papaya']

#3-insert() Add item at given index value
fruits.insert(1,"kiwi")
print(fruits) #['apple', 'kiwi', 'mango', 'banana', 'grapes', 'papaya']

#4-remove() Remove item by value 
fruits.remove("grapes")
print(fruits) #['apple', 'kiwi', 'mango', 'banana', 'papaya']

#5-pop() Remove item by index
fruits.pop(2)
print(fruits) #['apple', 'kiwi', 'banana', 'papaya']

#6-sort() Sory By Alphabetical Order or Numbers in ascending
fruits.sort()
print(fruits) #['apple', 'banana', 'kiwi', 'papaya']

#7-reverse() Reverse List
fruits.reverse()
print(fruits)#['papaya', 'kiwi', 'banana', 'apple']

#8-clear() Clear List but keep data structure as it is
fruits.clear()
print(fruits)#[] 