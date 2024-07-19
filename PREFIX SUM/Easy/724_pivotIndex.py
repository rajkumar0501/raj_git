class Solution:
    def pivotIndex(self, nums: [int]) -> int:

        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


    '''
        left_sum = []
        right_sum = []

        for i in range(len(nums)):
            left_sum.append(sum(nums[0:i]))


        for j in range(len(nums)):
            right_sum.append(sum(nums[j+1:len(nums)]))

        length = len(nums)
        k = 0

        while k < length:
            if right_sum[k] == left_sum[k]:
                return k
            k += 1

        return -1

    '''

solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6]))
