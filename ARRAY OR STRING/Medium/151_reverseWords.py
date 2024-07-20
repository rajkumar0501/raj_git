class Solution:
    def reverseWords(self, s: str) -> str:
        result = []

        w = ""

        s = s.strip()

        for word in s:
            if word == " ":
                w = w.strip()
                result.append(w)
                w = ""
            else:
                w = w + word

        w = w.strip()
        result.append(w)

        new = []

        for value in reversed(result):
            if not value == "":
                new.append(value)

        return ' '.join(new)

solution = Solution()
a = solution.reverseWords("a good   example")
print(f'"{a}"')
