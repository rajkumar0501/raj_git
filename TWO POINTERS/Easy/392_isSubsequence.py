class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) < 1:
            return True

        p = 0

        for i in range(0, len(t)):
            if s[p] == t[i]:
                p += 1
                if p == len(s):
                    return True

        return False



solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))

