#DAY1 and Day2

# string pattern match 
# first occurence 
# pattern filter 
# pattern split
# pattern replace
# patter  match

# program1 

# \w [a-z][A-Z][0-9]

import re
str = 'qas man sun mop run'
e1 = re.search(r'm\w\w',str)
if e1:
    print('pattern find')
    print(e1.group())
else:
    print('patter not found')

# program 2
str2 = 'qas man sun mop run'
e2 = re.findall(r'm\w\w',str2)
#[] falsy value
if e2:
    print('pattern found')
    for item in e2:
        print(item)
else:
    print('pattern not found')

#program 3
str3 ='mas man sun mop run'
e3 = re.match(r'm\w\w',str3)
if e3:
    print('match found')
    print(e3.group())
else:
    print('match not found')

#program 4
str4 = "i am learning javascript"
e4 = re.sub(r'javascript','java',str4)
print(e4)

# program5
#\W non alphanumeric not [a-z][A-Z][0-9]
str5 = 'This ; is the "Core" python\'s book'
e5 =re.split(r'\W+',str5)
print(e5)


#-----------------------------------------------------
#\w  ===>  [a-z] [A-Z][0-9]
#\b     ===> " "
#\W     ===> not [a-z][A-Z][0-9]
#\d     ===> [0,9]

str6 = 'an apple a day keeps the doctor away'
e6 = re.findall(r'\ba[\w]*\b',str6)
print(e6)


# DAY#
import re 
# [a-z A-Z 0-9]
str = 'an apple a day keeps doctor away'
e  = re.findall(r'a[\w]*',str)
print(e)

e2 = re.findall(r'\ba[\w]*\b',str)
print(e2)

#program2
str2 = 'The meeting will be conducted on 1st and 21st of every month'
e3 = re.findall(r'\d[\w]*',str2)
print(e3)

#program3
str2 = "one two three four five six seven 8 9 10"
e4 = re.search(r'\b\w{5}\b',str2)
print(e4.group())

e5 = re.findall(r'\b\w{5}\b',str2) #[a-zA-z0-9]
print(e5)

#program4 (four or more)
e6 = re.findall(r'\b\w{4,}\b',str2)
print(e6)

#program5(minimum3 and maximum5)

e6 = re.findall(r'\b\w{3,5}\b',str2)
print(e6)

#str2 = "one two three four five six seven 8 9 10"
e7 = re.findall(r'\b\d{1,}\b',str2)
print(e7)