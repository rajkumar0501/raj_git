class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:

        if k <= 1:
            return max(nums)


        length = len(nums)
        pointer1 = 0

        sum1 = sum(nums[0:k])

        highest = sum1

        pointer2 = k

        while length - k > 0:
            sum1 = sum1 - nums[pointer1] + nums[pointer2]

            if sum1 > highest:
                highest = sum1

            pointer1 += 1
            pointer2 += 1
            length -= 1

        max_avg = float(highest / k)

        return max_avg


solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
