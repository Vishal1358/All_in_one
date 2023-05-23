class Solution:
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     while m > 0 and n > 0:
    #         if nums1[m-1] >= nums2[n-1]:
    #             nums1[m+n-1] = nums1[m-1]
    #             m -= 1
    #         else:
    #             nums1[m+n-1] = nums2[n-1]
    #             n -= 1
    #     if n > 0:
    #         nums1[:n] = nums2[:n]
    #     return 
    def merge(self, nums1, m, nums2, n):
        idx = 0
        for i in range(len(nums1)):
            if idx >= n:
                break
            if nums1[i] == 0:
                nums1[i]=nums2[idx]
                idx += 1
        nums1.sort()

a = [1,2,3,0,0,0]
b = [2,5,6]
O = Solution()
print(O.merge(a, 3, b, 3))