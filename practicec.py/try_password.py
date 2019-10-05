import random

for i in range(50):
    pwd=random.randint(0,99999999)
    pwd_str=('%08d' %pwd)
    print(pwd_str)
print('---cutting line---')
a=('0','2','3','4','5','6','a','@','#','F')

for x in range(10):
    pwd_str=''
    for i in range(8):
        s=random.choice(a)
        pwd_str+=s
    print (pwd_str)
