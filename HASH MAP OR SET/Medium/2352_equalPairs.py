class Solution:
    def equalPairs(self, grid: [[int]]) -> int:

        dict = []

        for i in range(len(grid)):
            n = []
            for j in range(len(grid)):
                n.append(grid[j][i])
            dict.append(n)


        c = 0

        for i in dict:
            if i in grid:
                c += grid.count(i)

        return c

solution = Solution()
print(solution.equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))
