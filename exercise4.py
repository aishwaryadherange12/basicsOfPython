# 1. find data type of 
h0  = ()
print(type(h0))

h1  = ('GOA')
print(type(h1))

h2  = ('GOA',"PANJIM") 
print(type(h2))

# h3  = {GOA} #NameError: name 'GOA' is not defined
# print(type(h3)) #NameError: name 'GOA' is not defined 

# h4  = {GOA,"PANJIM"} 
# print(type(h4)) #NameError: name 'GOA' is not defined

# 2 . ADD "400076" IN BEOW SET

pin_mum = {400074,400075,400077}
a = pin_mum.add(400076)
print(a)

# 3 . SORT THE ITEMS IN THE BELOW SET
# ALSO REMOVE '0' FORM THE SET

runs_vk = {45,78,45,12,2,89,103,0}
b = sorted(runs_vk)
print(b)

# 4 . REMOVE '0' FORM THE SET 

runs_vk = {45,78,45,12,2,89,103,0}
runs_vk.remove(0)
print(runs_vk)#{2, 103, 89, 12, 45, 78}