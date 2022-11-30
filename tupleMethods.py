#cannot use append(),insert() ,remove(),extend(),pop(),clear()

#Methods in Tuple
#1.max()
marks= (90,50,56,46,85,72)
print(max(marks)) #90

#2.min()
print(min(marks)) #46

# 3.count()
num = (1,2,3,4,5,5,5,6,2,9,85)
print(num.count(5)) #3

#4.index()
b = num.index(85)  #10
print(b) 

#5.sorted()
c = sorted(num) #give list array
print(c) #[1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 9]

# id() function to get the memory location of the data
print(id(num))#2965822138560

#Convert List into tuple
d = tuple(c)
print(d)#(1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 9)
#Convert Tuple into List

e = list(d)
print(e)#[1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 9]
#in ==>Return boolean value
print("aishwarya" in ["aishwarya", "vaish","yashu"])

#not in ==>Return boolean value
print("ash" not in ["aishwarya", "vaish","yashu"])

fruits = ("mango","cheery","papapya","banana")
if("banana" in fruits):
    print("Fruit Is Available")
else:
    print("Fruit Is Not Available")