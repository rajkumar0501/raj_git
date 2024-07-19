class Solution:
    def longestSubarray(self, nums: [int]) -> int:

        length = len(nums)

        if not nums or length == 1:
            return 0

        right = 0
        left = 0
        max_length = 0
        k = 1

        while right < length:
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                else:
                    max_length = max(max_length, right - left)
                    if nums[left] == 0:
                        k += 1
                    left += 1
                    continue
            right += 1

        max_length = max(max_length, right - left)

        return max_length - 1



solution = Solution()
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))
