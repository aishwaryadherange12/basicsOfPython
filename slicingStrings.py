# 0 1 2 3 4 5 6 7 8
# a i s h w a r y a
#-9-8-7-6-5-4-3-2-1
name = 'aishwarya'

print(name[0])#a
print(name[6])#r
print(name[8])#a

#name[startPos:EndPos:Jump]
print(name[ :: ])#aishwarya
print(name[0:6]) # didint take 6th position =>aishwa
print(name[::2]) #jump 2 characters aswrya
print(name[-9:-1]) #aishwarya
print(name[-1:-9]) #empty
#To reverse string 
print(name[-1:-10:-1]) #ayrawhsia
print(name[::-1]) #ayrawhsia
