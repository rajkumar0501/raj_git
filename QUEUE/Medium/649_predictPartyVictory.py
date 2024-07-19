class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_queue = []
        d_queue = []
        length = len(senate)

        for i in range(length):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)


        while r_queue and d_queue:
            if r_queue[0] < d_queue[0]:
                r_queue.append(length)
            else:
                d_queue.append(length)

            r_queue.pop(0)
            d_queue.pop(0)
            length += 1

        if r_queue:
            return "Radiant"
        else:
            return "Dire"


solution = Solution()
print(solution.predictPartyVictory("RRDDDDDDDRRDRRDDRRRR"))

