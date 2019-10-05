import random
# 1)create
a = []

# 2)assignment
a = ['Micke', 'Paul']
b = [1, 2, 3]

print(a)
print(b)
print('----cutting line----')

# 3)append/extend
# a+=['Leon','Eathson'] or
a.append('Mike')

for i in range(1, 4):
    a.append('xxx')

print(a)
print('----cutting line----')

# extend
a.extend(b)
print(a)
print(b)
print('----cutting line----')

# joint
c = a + b
print(c)
print('----cutting line----')

# Lenth
lenth = len(a)
print('Lenth of lista is %d' % lenth)
print('----cutting line----')

# pick
index = 2
print(a[index])
print('----cutting line----')

# pick all
lenth = len(a)
for u in range(lenth):
    print(a[u])
print('----cutting line----')
# or
for i in a:
    print(i)

print('----cutting line----')
# pick randomly
for i in range(5):
    lucky = random.choice(a)
    print(lucky)
print('----cutting line----')
# change
a = ['Micke', 'Paul']
index = 0
a[index] = 'Mike'
print(a)
print('----cutting line----')
# Delete
a = ['Micke', 'Paul']
index = 0
del a[index]
print(a)
print('----cutting line----')
# clear
a.clear()
print(a)
print('----cutting line----')
