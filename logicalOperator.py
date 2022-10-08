#comparison Operator
e = 2
f = 3
print(2<3)
print(2>3)
print(2==3)
print(2!=3)
print(2<=3)
print(2>=3)

#logical operators
# and 
# True  and  True ------>  True
# False and  True ------>  False
# True  and  False ------> False
# False and  False ------> False

print(2 == 2 and 9 > 6)  # True
print(2 != 2 and 7 > 4)  # False
print(5 == 5 and 6 < 1)  # False
print(5 != 5 and 7 < 6)  # False


# or 
# True  or  True ------>  True
# False or  True ------>  True
# True  or  False ------> True
# False or  False ------> False

print(5 == 5 or 7 > 6)  # True
print(5 != 5 or 7 > 6)  # True
print(5 == 5 or 7 < 6)  # True
print(5 != 5 or 7 < 6)  # False

#not
#True  -- False
#False -- True 

print(not True)
print(not False)