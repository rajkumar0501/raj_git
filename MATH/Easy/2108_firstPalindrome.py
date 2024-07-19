class Solution:
    def firstPalindrome(self, words: [str]) -> str:

        for word in words:
            if word == word[::-1]:
                return word

        return ""

    
solution = Solution()
print(solution.firstPalindrome(["abc","car","ada","racecar","cool"]))
