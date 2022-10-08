#in variable declaration both variable allocates in different address
x = 10 
y = x
print(x)#10
print(y)#10

y = 900
print(x)#10
print(y)#99

# list 
# no new list form , new address form
# dono 1 address ko point karte hain
listX = [11,22,33]
listY = listX
print(listX)#[11, 22, 33]
print(listY)#[11, 22, 33]

listY[2] = 1000
print(listX)#[11, 22, 1000]
print(listY)#[11, 22, 1000]

#copy()
a  = [11,22,33]
b = a.copy() #beacuse of copy() list create new address for b
print(a)#[11, 22, 33]
print(b)#[11, 22, 33]

a[2] = 99

print(a)#[11, 22, 99]
print(b)#[11, 22, 33]