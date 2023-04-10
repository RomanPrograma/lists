
import random

list = []
for i in range(0, 6):
    list.append(random.randint(-20,20))
print(list)
#1
sum_negative = 0
for num in list:
    if num < 0:
        sum_negative += num
print('sum negative ',sum_negative)
#2
sum_of_even_numbers = 0
for num in list:
    if num %2 ==0:
        sum_of_even_numbers += num
print('sum of even numbers ', sum_of_even_numbers)
#3
sum_of_odd_numbers = 0
for num in list:
    if num %2 !=0:
        sum_of_odd_numbers += num
print('sum of odd numbers ',sum_of_odd_numbers)
#4
product_multiplie_of_3 = 1
for index, i in enumerate(list):
    if index %3 ==0:
        product_multiplie_of_3 *= i
print('product of numbers that are multiples of 3 ',product_multiplie_of_3)
#5
product_between_min_max = 1
max_index = list.index(max(list))
min_index = list.index(min(list))
if min_index > max_index:
    min_index, max_index = max_index, min_index
for num in list[min_index+1:max_index]:
    product_between_min_max *= num
print('product between min and max ',product_between_min_max)
#6
pos_indexes = [num for num in range(len(list)) if list[num] > 0]
if len(pos_indexes) > 1:
    first_pos_index = pos_indexes[0]
    last_pos_index = pos_indexes[-1]
    sum_between_pos = sum(list[first_pos_index+1:last_pos_index])
    print("sum between first pos and last pos: ", sum_between_pos)
else:
    print("It haven't two pos number.")






#max = max(list)
#indexOf = list.index(max)
#print('max_min ',max, min)
#print('max_min ',min * max)
