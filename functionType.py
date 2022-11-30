#1. Positional Argument
#2.Keyword Argument ==> To prevent Order Mismatch
#3.Default Argument =>if we did not give argument when calling function 
#4.Variable Length Argument ==>number of arguments unknown when we call function
#5. keyword variable length argument 

#1. Positional Argument
def calc(x,y):
    print(x+y)
#calc(1) #TypeError: calc() missing 1 required positional argument: 'y'   
calc(1,2)

#2.Keyword Argument ==> To prevent Order Mismatch
def address(city,state):
    print(city,state)
# address('MH','Sangamner') # so city = MH , state = Sangamner
address(state='MH',city='Sangamner') 

#3.Default Argument =>if we did not give argument when calling function 
# def calc1(a,b):
#     print(a+b)
# calc() #TypeError: calc() missing 2 required positional arguments: 'x' and 'y'

def calc1(a=10,b=5):
    print(a+b)
calc1() #Default Value is 10 and 5 if we did not give argument

#4.Variable Length Argument ==>number of arguments unknown when we call function
#Program 1
def nNumber(*args):
    print(args) #(1, 2, 3, 4, 5)
    print(type(args)) #tuple
nNumber(1,2,3,4,5)    
#Program 2
def nNumber1(*args):
    print(args) #(1, 2, 3, 4, 5)
    print(type(args)) #tuple
total=nNumber1(1,2,3,4,5) 
#program 3
def nNumber2(a,*args):
    print(a)
    print(args) # a= 1
nNumber2(1,2,3,4,5) #args = (2,3,4,5)    

#program 4

def nNumber3(*args):
    sum=0
    for i in args:
        sum = sum+i
        return sum
tot = nNumber3(1,2,3)
print("total",tot) # 6 

#5. keyword variable length argument 
#unknown key and values
def info(**kwark):
    return kwark
data = info(fName='aish',lName='D',age =24, city ="sangamner")    
for key,val in data.items():
    print(key,val)