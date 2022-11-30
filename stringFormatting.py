# The format() method formats the specified value(s) and insert them inside the string's placeholder. 
# The placeholder is defined using curly brackets: {}. 
#type 1
zero = 0
one  = 1 
two = 2 
print( "The numbers are " , zero ,one , two)
print(type(zero))
print( "The numbers are   {} {}  {}".format(zero,one,two))
print( "The numbers are   {0} {1}  {2}".format(zero,one,two))
print( "The numbers are   {2} {1}  {0}".format(zero,one,two))

# type 2
# #f-string latest method
print( f" using f string The numbers are {zero} {one}  {two} ")

q1 = "sun"
q2 = "moon"
q3 = "earth"
print(f"{0} is farthest from {1} and nearest is {2}")
