class Solution:
    def searchInsert(self, nums, target):
        idx = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target:
                idx = i + 1
            else:
                break
                
        return idx

a = [1,3,5,6]
t = 5
O = Solution()
print(O.searchInsert(a, t))