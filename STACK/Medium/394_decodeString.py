class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ''
        current_num = 0

        i = 0
        while i < len(s):
            if s[i].isdigit():
                start_num = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                current_num = int(s[start_num:i])
                i -= 1

            elif s[i] == "[":
                stack.append(current_str)
                stack.append(current_num)
                current_str = ''
                current_num = 0

            elif s[i] == "]":
                rep_times = stack.pop()
                prev_str = stack.pop()
                current_str = prev_str + current_str * rep_times

            else:
                current_str += s[i]

            i += 1


        return current_str

solution = Solution()
print(solution.decodeString("3[a2[c]]"))
