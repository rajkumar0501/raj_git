from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        queue = deque(list(range(1, n + 1)))

        j = 1

        while len(queue) > 1:
            if j == k:
                queue.popleft()
                j = 1
            else:
                queue.append(queue.popleft())
                j += 1

        return queue[0]

solution = Solution()
print(solution.findTheWinner(5, 2))
