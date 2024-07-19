class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        d = 1

        while n <= time:
            time = time - (n -1)
            d = d * (-1)

        if d == 1:
            index = time + 1
        elif d == -1:
            index = n - time

        return index



solution = Solution()
print(solution.passThePillow(2, 341))
