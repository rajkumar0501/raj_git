class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        r = ""

        while i < len(word1) and j < len(word2):
            r += word1[i] + word2[j]
            i += 1
            j += 1

        while i < len(word1):
            r += word1[i]
            i += 1

        while j < len(word2):
            r += word2[j]
            j += 1

        return r

solution = Solution()
print(solution.mergeAlternately('abc','pqrs'))

