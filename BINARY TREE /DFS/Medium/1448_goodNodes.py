class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, mxVal):
            if not node:
                return 0

            if node.val >= mxVal:
                good = 1
            else:
                good = 0

            mxVal = max(mxVal, node.val)

            good += dfs(node.left, mxVal)
            good += dfs(node.right, mxVal)

            return good

        return dfs(root, root.val)



root = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(4)


solution = Solution()

goodNodes = solution.goodNodes(root)
print(goodNodes)

