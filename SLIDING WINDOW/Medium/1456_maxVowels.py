class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = "aeiou"
        max_v = 0
        current = 0

        for i in range(k):
            if s[i] in vowels:
                current += 1

        max_v = current

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current -= 1
            if s[i] in vowels:
                current += 1
            max_v = max(current, max_v)

        return max_v
    

solution = Solution()
print(solution.maxVowels("abciiidef", 3))
