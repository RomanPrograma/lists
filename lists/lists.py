

from operator import indexOf
import random

list = []
for i in range(0, 12):
    list.append(random.randint(-10,10))
print(list)
sum_negative = 0
for num in list:
    if num < 0:
        sum_negative += num
print('sum negative ',sum_negative)

sum_of_even_numbers = 0
for num in list:
    if num %2 ==0:
        sum_of_even_numbers += num
print('sum of even numbers ', sum_of_even_numbers)

sum_of_odd_numbers = 0
for num in list:
    if num %2 !=0:
        sum_of_odd_numbers += num
print('sum of odd numbers ',sum_of_odd_numbers)

product_multiplie_of_3 = 1
for index, i in enumerate(list):
    if index %3 ==0:
        product_multiplie_of_3 *= i
print('product of numbers that are multiples of 3 ',product_multiplie_of_3)
max = max(list)
min = min(list)
indexOf = list.index(max)
print('max_min ',max, min)
print('max_min ',min * max)








#sum_of_even_numbers = 0
#for num in list:
   # if num >0:
    #    Break
  #  if num = max(list):
    #   Break
     #   print(num)
    #    sum_of_even_numbers += num
#print('sum of even numbers ', sum_of_even_numbers)
