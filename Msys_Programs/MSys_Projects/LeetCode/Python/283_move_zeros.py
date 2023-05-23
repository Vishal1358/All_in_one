nums = [0,1,0,3,12]
i = 0
for j in range(len(nums)):
    if nums[i]==0 and nums[j] != 0:
        nums[i], nums[j] = nums[j],nums[i]
    if (nums[i]!=0):
        i+=1
print(nums)
