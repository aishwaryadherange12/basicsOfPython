# 1. FIND THE DATA TYPE AND LENGHT OF z
from itertools import count
z = "Repetition is the mother of learning"
a = type(z)
print(a)

# 2 . REVERSE THE STRING USING NEGATIVE INDEXING/SLICING 

k  = "Was it a car or a cat I saw? "
p = "Do geese see God?"

print(k[::-1])
print(p[::-1])

# 3 . PRINT THE FOLLOWING USING range()

h = "HYDERABAD"
c = "CHENNAI"
d = "DELHI"

for i in range(len(h)):
    print(h[i])

for i in range(len(c)):
    print(c[i])

for i in range(len(d)):
    print(d[i])

# 4.  find number of spaces in song2
#     find count of Ganga in song2
#     replace  Ganga with "GANGA" in song2

song2 = '''
Jana Gana Mana Adhinaayak Jaya Hey, 
Bhaarat Bhaagya Vidhaataa 
Panjaab Sindhu Gujarat Maraatha, 
Draavid Utkal Banga 
Vindhya Himaachal Yamuna Ganga, 
Vindhya Himaachal Yamuna Ganga, 
Uchchhal Jaladhi Taranga
Tav Shubh Naamey Jaagey, 
Tav Shubh Aashish Maange Gaahey 
Tav Jayagaathaa 
Jana Gana Mangal Daayak, Jaya Hey Bhaarat Bhaagya Vidhaataa 
Jaya Hey, 
Jaya Hey, 
Jaya Hey, 
Jaya Jaya jaya, 
Jaya Hey
'''
b = song2.count(" ")
print(b)

c = song2.count("Ganga")
print(c)

d = song2.replace("Ganga","GANGA")
print(d)