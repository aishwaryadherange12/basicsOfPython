# # any type of editing is not supported in a tuple ie cannot change
# # immutable
# # data[4] = 99 #does not support item assignment
# # unique representation/address
# # hashable / fingerprint
#cannot use append(),insert() ,remove(),extend(),pop(),clear()

# # changable/mutable  : unhashable eg: list
# # unchangable/immutable :  hashable eg : tuple

# a =(1,2,3,4,5)
# a[2] = 22 //cannot update
# print(a)#error
# Tuple Stores with index
data = ("aish ","d",25)
print(data[0]) #aish
print(data[1]) #d
print(data[2]) #25