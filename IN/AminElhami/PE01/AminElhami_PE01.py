
nums = [0,1]
i = 2
while i<=100:
    nums.append(float(nums[i-1])**0.5+float(nums[i-2])**1.1)
    print(str(nums[i]))
    i=i+1