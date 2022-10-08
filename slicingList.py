# slicing
#           0       1          2          3       4 
cities = ["pune","nagpur","banglore","chennai","kolkata"]
#         -5      -4          -3         -2      -1

a2 = cities[1] #nagpur
a3 = cities[-4] #nagpur
print(a2)
print(a3)
#[startIndex:endIndex:steps(by default1)]
a4 = cities[1:4]
print(a4)  #['nagpur', 'banglore', 'chennai']

a5 =cities[1:4:2] #2 jump 
print(a5)#['nagpur', 'chennai']

# reverse list
a6 = cities[::-1]
print(a6)
#or

a6 = cities[-1:-6:-1]
print(a6)
