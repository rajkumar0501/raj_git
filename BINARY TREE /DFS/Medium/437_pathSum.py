class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: [TreeNode], targetSum: int) -> int:

        def path(root, tsum):
            if not root:
                return 0

            return path(root.left, tsum) + path(root.right, tsum) + newpath(root, tsum)


        def newpath(node, tsum):
            if not node:
                return 0

            count = 1 if node.val == tsum else 0

            count += newpath(node.left, tsum - node.val)
            count += newpath(node.right, tsum - node.val)

            return count

        return path(root, targetSum)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)


solution = Solution()
count = solution.pathSum(root, 8)
print(count)
