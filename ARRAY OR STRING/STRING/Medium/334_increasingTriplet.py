class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:

        i = float('inf')
        j = float('inf')

        for num in nums:
            if num <= i :
                i = num
            elif num <= j:
                j = num
            else:
                return True

        return False


solution = Solution()
print(solution.increasingTriplet([20,100,10,12,5,11]))
