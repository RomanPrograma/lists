nums = input("enter numbers: ").split()
nums = [int(num) for num in nums]

min_index = nums.index(min(nums))
max_index = nums.index(max(nums))

nums[min_index], nums[max_index] = nums[max_index], nums[min_index]

print("List with changed places of minimum and maximum elements:")
print(nums)
