class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        sum = numBottles

        temp = numBottles

        while temp >= numExchange:

            div = temp // numExchange
            rem = temp % numExchange
            temp = div + rem
            sum += div



        return sum




solution = Solution()
print(solution.numWaterBottles(9, 3))
