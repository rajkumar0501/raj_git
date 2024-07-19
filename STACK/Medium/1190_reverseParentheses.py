class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []
        m = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    idx = stack.pop()
                    m.append((idx, i))


        list = []

        for k in s:
            list.append(k)


        j = 0
        l = len(m)


        while j < l:
            v1 = m[j][0]
            v2 = m[j][1]
            while v1 < v2:
                list[v1], list[v2] = list[v2], list[v1]
                v1 += 1
                v2 -= 1

            j += 1


        output = ""


        for x in list:
            if x != "(" and x != ")":
                output += x


        return output



solution = Solution()
print(solution.reverseParentheses("a(bcdefghijkl(mno)p)q"))

