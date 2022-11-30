# packing/unpacking
#      0  1  2   3 
t1  = (5,55,555,5555)
print(t1[0]) #5
print(t1[1]) #55
print(t1[2]) #555


a ,b, c ,d = t1

print(a)
print(b)
print(c)
print(d)

# a ,b, c = t1 #too many values to unpack

# a ,b, c ,d,f = t1 #not enough values to unpack

# #       0     1    2    3
city = ('P', 'U', 'N', 'E') #packing 

# print(city[0]) #P
# print(city[1]) #U
# print(city[2]) #N
# print(city[3]) #E

a ,b ,c ,d = city #unpacking
# print(a) #P
# print(b) #U
# print(c) #N
# print(d) #E

# palce holder

a ,b ,_ ,_ = city # _ is a placeholder

print(b) #U
print(_) # E latest value not N

