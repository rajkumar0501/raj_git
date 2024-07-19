class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:

        stack = [[root, 1]]

        r = 0

        while stack:
            node, depth = stack.pop()

            if node:
                r = max(r, depth)

                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return r


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


solution = Solution()

max_depth = solution.maxDepth(root)
print(max_depth)
