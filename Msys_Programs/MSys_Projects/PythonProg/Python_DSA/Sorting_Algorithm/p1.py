class Solution:

    def twosum(self, num:list[int()],target:int):
        for i, right[int] in range(num):
            for j, left in range(num):
                if right+left==target and i!=j:
                    return i,j
        # return None

a = [5,6,8,2]
t = 11
b = Solution()
# b.twosum(a, t)
print(b.twosum(a, t))