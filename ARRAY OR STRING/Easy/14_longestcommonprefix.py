class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""

        if any(not s for s in strs):
            return ""

        if len(strs) == 1:
            return strs[0]

        output = []

        min_len = min(len(s) for s in strs)

        if min_len < 1:
            return ''.join(strs)

        for i in range(min_len):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return ''.join(output)
            output.append(strs[j][i])

        return ''.join(output)


solution = Solution()
s = solution.longestCommonPrefix(["","b"])
print(f'"{s}"')
