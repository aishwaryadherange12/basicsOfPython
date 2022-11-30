names = ['pooja','aish','vaish']
names2 = names
names2[0] = "vaish"

print(names)#['vaish', 'aish', 'vaish']
print(names2)#['vaish', 'aish', 'vaish']

a = names.copy()

a[0] = "yahu"
print(a)#['yashu', 'aish', 'vaish']
print(names)#['vaish', 'aish', 'vaish']
j = {
    's1':45,
    's2':90
}
k = j
k['s1'] = 100
print(k)#{'s1': 100, 's2': 90}
print(j)#{'s1': 100, 's2': 90}

z = k.copy()
z['s1'] = 500
print(z)#{'s1': 500, 's2': 90}
print(k) #{'s1': 100, 's2': 90}