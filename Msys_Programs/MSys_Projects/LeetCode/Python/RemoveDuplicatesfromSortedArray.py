class Solution:
    def removeDuplicates(self, nums):
        nums.extend(sorted(set(nums) ,reverse= True))
        nums.reverse()
        print(list(set(nums)))
    

O = Solution()
# L = [0,0,1,1,1,2,2,3,3,4]
L = [2,2,3,3,4,4,5,5,6]
print("Orignal list: ",L)
p = O.removeDuplicates(L)
print(p)