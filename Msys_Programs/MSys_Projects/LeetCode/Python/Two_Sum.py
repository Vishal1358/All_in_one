class Solution:
    def twoSum(self,List, target):
        check = set()
        for i in range(len(List)):
            if List[i] in check:
                return [List.index(target - List[i]), i]
            else:
                check.add(target - List[i])


TS = Solution()
B = TS.twoSum([2, 7, 11, 15], 9)
print(B)