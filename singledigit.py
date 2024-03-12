nums = [4]
xor = nums[0]
for i in range(1, len(nums)):
    xor = xor^nums[i]
print(xor)

