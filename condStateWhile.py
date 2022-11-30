# break use to break the condn
# cont
# #In while loop first statement execute then condition check  
# i = 1
# #print 1 to 10
# while i<=10: #1<10, 2<10, 10<10=False Exit Loop 
#     #print(i) #goes to infinite loop and print infinite 1 
#     i=i+1 #0+1=1 , 1+1=2,.....,9+1 = 10 
#     print(i) #1, 2, .... ,10
#     #thats why it prints 10 also
q = 5
while(q>=1):
    if(q==2):
        q=q-1
        continue
    print(q)
    q = q-1
# q = 10
# while(q>=1):
#     print(q)
#     if(q==6):
#         break
#     q = q-1