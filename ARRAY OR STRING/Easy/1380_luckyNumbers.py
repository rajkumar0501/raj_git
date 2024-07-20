class Solution:
    def luckyNumbers(self, matrix: [[int]]) -> [int]:

        l1 = []
        l2 = []

        for i in range(len(matrix)):
            min_n = float('inf')
            for j in range(len(matrix[i])):
                if matrix[i][j] < min_n:
                    min_n = matrix[i][j]
            l1.append(min_n)


        for k in range(len(matrix[0])):
            max_n = float('-inf')
            for l in range(len(matrix)):
                if matrix[l][k] > max_n:
                    max_n = matrix[l][k]
            l2.append(max_n)

        output = []

        for x in l1:
            for y in l2:
                if x == y:
                    output.append(x)

        return output

solution = Solution()
print(solution.luckyNumbers([[76618,42558,65788,20503,29400,54116]]))
