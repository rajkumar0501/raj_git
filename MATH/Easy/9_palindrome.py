class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True

        newx = 0
        tempx = x
        while tempx != 0:
            rem = tempx % 10
            newx = newx * 10 + rem
            tempx = tempx // 10

        return x == newx


solution = Solution()
print(solution.isPalindrome(9999))
