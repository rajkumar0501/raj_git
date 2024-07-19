class Solution:
    def moveZeroes(self, nums: [int]) -> None:

        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(len(nums) - 1):
                    if nums[j] == 0:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

        '''
        p = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        return nums

        '''

solution = Solution()
print(solution.moveZeroes([0,0,1]))
