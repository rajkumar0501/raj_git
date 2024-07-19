class Solution:
    def majorityElement(self, nums: [int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n // 2]


solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2]))
