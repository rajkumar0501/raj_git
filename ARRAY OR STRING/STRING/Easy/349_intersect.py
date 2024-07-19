from collections import Counter

class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:

        count1 = Counter(nums1)
        output = []

        for num in nums2:
            if num in count1 and count1[num] > 0:
                output.append(num)
                count1[num] -= 1  

        return output


solution = Solution()
print(solution.intersect([4,9,5], [9,4,9,8,4]))
