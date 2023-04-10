nums = input("enter numbers: ").split()
nums = [int(num) for num in nums]

average = sum(nums) / len(nums)

count = 0
for num in nums:
    if num > average:
        count += 1

print("The number of numbers greater than the arithmetic mean:", count)
