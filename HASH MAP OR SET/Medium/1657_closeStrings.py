class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        h1 = {}
        h2 = {}

        for i in word1:
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1

        for j in word2:
            if j in h2:
                h2[j] += 1
            else:
                h2[j] = 1


        return sorted(h1.values()) == sorted(h2.values()) and sorted(h1) == sorted(h2)

        '''
        l1, l2 = [], []

        for i in set(word1):
            l1.append(word1.count(i))
            l2.append(word2.count(i))

        l1.sort()
        l2.sort()

        return l1 == l2

        '''

solution = Solution()
print(solution.closeStrings("a", "aa"))
