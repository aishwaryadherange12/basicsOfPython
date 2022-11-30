# to reduce line of code
# types of function
    # inbuilt fun
    # custom / user defined
    # lambda

# sum of two numbers

x = 100
y = 10
z = x + y 
print(z)
# syntax 
'''
def name_of_function(x,y,z,....):
    code 
'''
#def is keyword, x,y ==> parameter
# 1st program

# without paramaters
#declaration
def calc():
    print(5+5)
#calling function
calc()    #arguments

# 2nd program
# with paramaters
def calc(x,y):
    z = x+y
    print(z)
#calling function multiple time
calc(1,2)    
calc(5,5) #5 => argument

# function that returns some value
def calc(x,y):
    return x+y
#calling function multiple time with return type
result = calc(50,10)
avg = result/2
print(result,avg) #60 30.0
print(type(result)) #<class 'int'>
print(type(avg)) #<class 'float'>

def func2(x,y,z):
    pass
print(func2(10,20,30)) #none

# even or odd 
q3 = 100
if(q3 % 2 == 0):
    print("number is even")
else:
    print("number is odd")

# avoid repeattion using function
def even_odd(x):
    if(x % 2 == 0):
        print("number is even")
    else:
        print("number id odd")

even_odd(12)
even_odd(13)

