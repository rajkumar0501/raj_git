class Solution:
    def maxArea(self, height: [int]) -> int:

        max = 0
        length = len(height)
        left = 0
        right = length - 1


        while length > 0:
            if height[right] > height[left]:
                h = height[left]
                x = h * (right - left)
                if x > max:
                    max = x

                left += 1
                length -= 1

            else:
                h = height[right]
                x = h * (right - left)
                if x > max:
                    max = x

                right -= 1
                length -= 1


        return max


solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
