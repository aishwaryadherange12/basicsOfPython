#1- upper() => Convert string into upper case
firstName = "aishwarya"
print(firstName.upper()) #AISHWARYA
print(firstName) #aishwarya

#2- lower() => Convert string into lower case
lastName = "DHERANGE"
print(lastName.lower()) #aishwarya
print(lastName)#AISHWARYA

#3- islower() => Check String is in lower case
#4- isupper() => Check String is in upper case
#if mixed string then both methods false

print("Is Upper First Name=> ", firstName.isupper()) #false
print("Is Lower First Name=> ",firstName.islower())  #true   

print("Is Upper Last Name=> ", lastName.isupper())   #true   
print("Is Lower Last Name=> ",lastName.islower())    #false

#5- capitalize() => Convert first letter into Upper Case and remaining into lower case
city = "sangamneR"
print(city.capitalize()) #Sangamner

#6- startswith() => return boolean value
city1 = "pune"
print(city1.startswith("p")) #true

#7- endswith() => return boolean value
city6 = "nashik"
print(city6.endswith('ik')) #true

#8- index() => Return index of character
# a i s h w a r y a
# 0 1 2 3 4 5 6 7 8
name = "Aishwarya"
print(name.index('A')) #0
print(name.index('a')) #5 first occurance
print(name.index('Ai'))#0
#print(name.index('z')) #error subtring not found terminate

#9- count() => Count character or substring ocuurances
print("Count=> ",name.count('wa')) #2
print("Count=> ",name.count('z')) #0

#10- replace => Replace the string
str1 = "I am Learning Java"
finalStr = str1.replace('Java', 'Python')
print(finalStr)