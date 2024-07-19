class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)



solution = Solution()
print(solution.removeStars("il**autonrd**cl**nh*up*afpizp****d*a****lst"))
