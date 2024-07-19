class Solution:
    def largestAltitude(self, gain: [int]) -> int:

        alt = []

        alt.append(0)

        for i in range(len(gain)):
            new = alt[i] + gain[i]
            alt.append(new)


        return max(alt)

solution = Solution()
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))
