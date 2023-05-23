class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x>=0):
            return x == int(str(x)[::-1])
        return False

P = Solution()
print(P.isPalindrome(233))
print(P.isPalindrome(212))
print(P.isPalindrome(21212))
print(P.isPalindrome(320023))