class Solution:
    def averageWaitingTime(self, customers: [[int]]) -> float:

        arrive = 0
        n = len(customers)
        sum = customers[0][0]
        time = 0

        while arrive < n:
            if sum >= customers[arrive][0]:
                sum += customers[arrive][1]
            else:
                sum = customers[arrive][0] + customers[arrive][1]

            time += sum - customers[arrive][0]
            arrive += 1


        return float(time/n)




solution = Solution()
print(solution.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
