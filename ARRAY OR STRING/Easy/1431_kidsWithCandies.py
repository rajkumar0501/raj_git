class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        result = []


        for i in range(len(candies)):
            total = candies[i] + extraCandies
            r = True
            for j in range(len(candies)):
                if total < candies[j]:
                    r = False
                    break

            result.append(r)

        return result



solution = Solution()
print(solution.kidsWithCandies([4,2,1,1,2], 1))

