class Solution:
    def minOperations(self, logs: [str]) -> int:

        l = ["../", "./" , "x/"]

        main = 0

        for i in logs:
            if i not in l:
                main += 1
            if i in l:
                if i == "../":
                    if main > 0:
                        main -= 1
                elif i == "x/":
                    main += 1


        return main



solution = Solution()

print(solution.minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))
