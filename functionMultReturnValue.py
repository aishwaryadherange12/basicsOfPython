# function returning more than one value 
# def calculator(a,b):
#     q1 = a + b
#     q2 = a - b
#     q3 = a * b
#     q4 = a / b
#     q5 = a % b
#     return q1

# q2 = calculator(12,1)
# print(q2)
################################################
# list , tuple , dictionary , set
#1. list
def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return [q1,q2,q3,q4,q5]
listC = calculator(12,1)
print(listC)#[13, 11, 12, 12.0, 0]

#2. tuple 
def calc(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return (q1,q2,q3,q4,q5)
    
print(calc(10,5)) #(15, 5, 50, 2.0, 0)

#3. set 
def calc1(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return {q1,q2,q3,q4,q5}
#Set value return values without sequence    
print(calc1(10,5)) #{0, 2.0, 5, 15, 50} 

#4. Dictionary
def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return {
        'addition':q1,
        'subtraction':q2,
        'multiplication':q3,
        'division':q4,
        'modulus':q5
        }
listE = calculator(12,1)
print(listE)

def addA(a,b):
    print(a+b)
print(addA) #print only function      
def addB(x,y,fn):
    fn = x+y
    print(fn)
addB(2,4,addA)
