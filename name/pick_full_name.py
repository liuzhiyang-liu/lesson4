# -*- coding: UTF-8 -*-

import random

print('-----cutting line-----')
family_words = ("赵", "钱", "孙", "李", "周", "吴", "郑", "王")

given_words = ["致浩", "明云", "浩烨", "兆忠", "予忻", "顺雨", "尚扬", "俊祥", "语禅", "予浩"]
given_words1 = [ \
"潮","彻","郴","琛","澈","臣","辰","晨","承","盛","程", "池", \
"炽","冲","重","崇","绸","畴","酬","筹","楚","处" \
]
given_words.extend(given_words1)

sex = ('male', 'female')

class_name=[]

for i in range(30):

    full_name=''
    fname=random.choice(family_words)
    gname=random.choice(given_words)
    full_name1=fname + " " + gname
    '''print(full_name1)'''

    s_sex = random.choice(sex)
    student=(full_name1,s_sex)
    print(student)

    class_name.append(student)

print(class_name)
