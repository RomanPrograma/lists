import random
list=[]
for i in range(10):
    list.append(random.randint(1, 100))
print(list)

even_count = 0
odd_count = 0

for num in list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Кількість парних чисел:", even_count)
print("Кількість непарних чисел:", odd_count)