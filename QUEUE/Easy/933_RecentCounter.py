import collections

class RecentCounter:

    def __init__(self):
        self.que = collections.deque()


    def ping(self, t: int) -> int:
        self.que.append(t)
        while self.que[0] < t - 3000:
            self.que.popleft()

        return len(self.que)



obj = RecentCounter()
print(obj.ping(1), obj.ping(100), obj.ping(3001), obj.ping(3002), obj.ping(6000), obj.ping(9000))

