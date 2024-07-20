class Solution:
    def restoreMatrix(self, rowSum: [int], colSum: [int]) -> [[int]]:
        x, y = len(rowSum), len(colSum)

        r = [[0]* y for _ in range(x)]

        for i in range(x):
            r[i][0] = rowSum[i]

        for j in range(y):
            c_sum = 0
            for k in range(x):
                c_sum += r[k][j]

            k = 0
            while c_sum > colSum[j]:
                d = c_sum - colSum[j]
                s = min(r[k][j], d)
                r[k][j] -= s
                r[k][j + 1] += s
                c_sum -= s
                k += 1

        return r

solution = Solution()
print(solution.restoreMatrix([5,7,10], [8,6,8]))
