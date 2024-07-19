class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        len1 = len(str1)
        len2 = len(str2)

        div_len = gcd(len1, len2)
        div = str1[:div_len]

        if str1 + str2 == str2 + str1:
            return div
        else:
            return ''


solution = Solution()
s = solution.gcdOfStrings("ABCABC", "ABC")
print(f'"{s}"')
