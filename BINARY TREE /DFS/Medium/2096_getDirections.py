class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: [TreeNode], startValue: int, destValue: int) -> str:


        def dfs(node, path, t):
            if not node:
                return ""

            if node.val == t:
                return path

            path.append("L")
            r = dfs(node.left, path, t)
            if r:
                return r

            path.pop()
            path.append("R")
            r = dfs(node.right, path, t)
            if r:
                return r

            path.pop()
            return ""

        s_path = dfs(root, [], startValue)
        d_path = dfs(root, [], destValue)

        i = 0
        while i < min(len(s_path), len(d_path)):
            if s_path[i] != d_path[i]:
                break
            i += 1

        return "".join(["U"] * len(s_path[i:]) + d_path[i:])


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)


solution = Solution()
print(solution.getDirections(root, 3, 6))

