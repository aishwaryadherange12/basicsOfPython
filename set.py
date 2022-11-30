# A set object is an 
# unordered 
# collection of objects
# distinct hashable objects. 
# hashable = unique element or object
#unhashable = different
# Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.
# #eg. 

# s_even = {True, False, False ,25 , 'order' , [55,55,55]} # error unhashable type: 'list'
set1 = {True, False, False ,25 , 'order' } #unhashable type: 'list'

print(set1)#{False, True, 25, 'order'}

print(type(set1))#<class 'set'>

# print(set1[0])#error 'set' object is not subscriptable
#set alement is not stored with index same as object

set_one = {'R', 'R', 'R', 'R', 'R', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'R', 'R', 'R', 'R', 'R', 'R', 'A', 'A', 'A'}
#remove all duplicate elements
print("Length is=> ",len(set_one))#Length is=>  3
print(set_one)#{'S', 'A', 'R'}
# # typecasting 

print(list(set_one))#['A', 'S', 'R']
