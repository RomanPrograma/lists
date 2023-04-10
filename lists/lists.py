
import random
list = []
for i in range (13):
    list.append(random.randint(-10, 10))
print(list)

for i in list:
    if  i %2==0:
       
        print('pair',i )
print()
odd=0
for i in list:
    if  i%2 != 0:
        odd=i
        print('odd', odd)
print()
neg=0
for i in list:
    if i<0:
        neg=i
        print('neg', neg)
print()
pos=0
for i in list:
    if i>0:
        pos=i
        print('pos', pos)