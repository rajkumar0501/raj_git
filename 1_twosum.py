class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i, j]

        return []

solution = Solution()
print(solution.twoSum([2,7,11,15], 13))
