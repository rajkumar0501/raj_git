class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        self.ans = 0

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for x in left:
                for y in right:
                    if x + y <= distance:
                        self.ans += 1
            total = left + right
            return [dist + 1 for dist in total]


        dfs(root)
        return self.ans



root = TreeNode(7)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(2)





solution = Solution()
print(solution.countPairs(root, 3))

