s = input("Enter String ")
# for i in range(len(s)):
#     if s[i].isalnum() == True:
#         print(True)
#         break
#     elif s[i].isalnum() == False:
#         pass
#     else:
#         print(False)
        
s = input("Enter the string:")
for i in range(len(s)):
    if s[i].islower() == True:
        print(True)
        break
    else :
        if s[i].islower() == False:
            i = i +1
            if i == len(s):
                print(False)