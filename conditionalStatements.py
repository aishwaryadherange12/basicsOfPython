#Conditional Statement
#Single Input ===> Multiple Output
# if(condition):
#     statement 1
# else:
#     statememt 2

#Discount on tickets
#o/p=> You got 10% Discount
noOfTickets = 8
if(noOfTickets > 0 and noOfTickets <5 ):
    print("You got 5% Discount")
elif(noOfTickets >=5 and noOfTickets <10 ):
    print("You got 10% Discount")
elif(noOfTickets >= 10 and noOfTickets <20 ):
    print("You got 15% Discount")
elif(noOfTickets >= 20):
    print("You got 20% Discount")
else:
    print("Enter Valid Number Of Ticktes")    

#Grades => Print All Values if all condition are true
#o/p=> Grade A, Grade B, Grade C, Grade D
marks = 91
if marks > 90:
    print("Grade A")
if marks > 80:
    print("Grade B")
if marks > 70:
    print("Grade C")
if marks > 60:
    print("Grade D")
#Grades => Print when first condtion is true and exit
#o/p=> Grade A
marks = 91
if marks > 90:
    print("Grade A")
elif marks > 80:
    print("Grade B")
elif marks > 70:
    print("Grade C")
elif marks > 60:
    print("Grade D")