class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        text = list(s)

        position = []

        for i in range(len(text)):
            if text[i] in vowels:
                position.append(i)

        for i in range(len(position) // 2):
            text[position[i]], text[position[(len(position) - 1) - i]
                                    ] = text[position[(len(position) - 1) - i]], text[position[i]]

        return ''.join(text)


solution = Solution()

print(solution.reverseVowels("lEetcode"))
