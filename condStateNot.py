# #in return boolean value  
# fruits = ["mango", "banana", "apple", "cherry"]
# if ("kiwi" in fruits):
#     print("Fruit Is Available")
# else:
#     print("Fruit Is Not Available")
# #not return boolean value 
#     if("banana" not in fruits):
#         print("Fruit Is Not Available")
#     else:
#         print("Fruit Is Available")
fruits = ["mango", "banana", "apple", "cherry"]
item = input("Enter Fruit Name To check its available or not=>")
if(item in fruits):
    print(item," Is Available")
else:
    print(item, " Is Not Available" )