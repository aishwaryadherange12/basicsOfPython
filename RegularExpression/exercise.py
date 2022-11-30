import re
str1 = "chinmay got 56 marks and rahul got 90 marks"
#o/p=>[56,90]
a1 = re.findall(r'\d{1,2}',str1) 
#print(a1)
for i in a1:
    print(i)
str2 = "The meeting will start at 9am and will end at 8pm . please join at 8am"
#o/p=>[9am 8am 9pm]
a2 = re.findall(r'\d{1}\w\w',str2)
#print(a2)
for i in a2:
    print(i)