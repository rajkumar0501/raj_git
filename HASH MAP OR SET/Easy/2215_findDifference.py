class Solution:
    def findDifference(self, nums1: [int], nums2: [int]) -> [[int]]:

        n1 = []
        n2 = []

        for num in nums1:
            if num not in nums2 and num not in n1:
                n1.append(num)

        for num in nums2:
            if num not in nums1 and num not in n2:
                n2.append(num)


        return [n1, n2]


solution = Solution()
print(solution.findDifference([1,2,3], [2,4,6]))
