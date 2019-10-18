import random
a = ['abc']

print(a)

a.append('mike')
print(a)

a +=['bacd']
print(a)

for i in range(1, 4):
    a.append('xxx')
print (a)

b = ['666']
a.extend(b)
print (a)

a.extend('bbb')
print(a)

c = a + b
print(c)

lenth =len(a)
print('lenth of aaaa is %d' %lenth)

i = 2
print(a[i])

l=len(a)
for k in range(l):
    print(a[k])

for t in range (8):
    luck=random.choice(a)
    print (luck)
print('-------------------------------------')
a = ['Micke', 'Paul']
index = 0
a[index] = 'Mike'
print(a)
print('----cutting line----')

a = ['Even dead, I am the heros', 'hhhh']
ko = (0)
del a[ko]
print (a)
