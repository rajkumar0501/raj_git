class Solution:
    def longestOnes(self, nums: [int], k: int) -> int:

        length = len(nums)

        if not 0 <= k <= length:
            return 0


        max_len = 0
        left = 0
        right = 0


        while right < length:
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                else:
                    max_len = max(max_len, right - left)
                    if nums[left] == 0:
                        k += 1
                    left += 1
                    continue
            right += 1

        max_len = max(max_len, right - left)
        
        return max_len


solution = Solution()
print(solution.longestOnes([0,0,0,1], 4))
