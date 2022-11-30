# string pattern match 
# first occurence 
# pattern filter 
# pattern split
# pattern replace
# patter  match
 
# \w [a-z][A-Z][0-9]

# program1
import re
str1 = "qas man sun mop run mad"
a1 = re.search(r'm\w\w',str1)
print(a1) # <re.Match object; span=(4, 7), match='man'>
print(a1.group()) #man
#we have to group to print answer 

#Program 2
a2 = re.findall(r'm\w\w',str1)
print(a2) #['man', 'mop', 'mad']

for i in a2:
    print(i) # man mop mad

#Program 3
str3 ='mas man sun mop run'
e3 = re.match(r'm\w\w',str3) #return true or false
if e3:
    print('match found')
    print(e3.group())
else:
    print('match not found')