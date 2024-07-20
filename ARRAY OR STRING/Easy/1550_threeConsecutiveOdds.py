class Solution:
    def threeConsecutiveOdds(self, arr: [int]) -> bool:

        count = 0

        for num in arr:
            if (num % 2) == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False


solution = Solution()
print(solution.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))