class Solution:
    def minDifference(self, nums: [int]) -> int:

        if len(nums) < 4:
            return 0

        nums.sort()

        nums1 = nums[-4] - nums[0]

        nums2 = nums[-1] - nums[3]

        nums3 = nums[-3] - nums[1]

        nums4 = nums[-2] - nums[2]

        output = min(nums1, nums2, nums3, nums4)

        return output

solution = Solution()
print(solution.minDifference([6, 6, 0, 1, 1, 4, 6]))
