class Solution:
    def search(self, nums, target):
        index = 0
        while index < len(nums):
            if nums[index] == target:
                return index
            index = index + 1
        return -1

O = Solution()
print(O.search([2,4,5,6,7], 5))
print(O.search([2,4,5,6,7], 8))
print(O.search([2,4,5,6,7], 6))