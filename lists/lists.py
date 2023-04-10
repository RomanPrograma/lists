nums = input("enter numbers:  ").split()
nums = [int(num) for num in nums]

positive_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)

print("Positive numbers in the list: ", positive_nums)
