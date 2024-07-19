from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: [TreeNode], to_delete: [int]) -> [TreeNode]:

        to_delete = set(to_delete)
        result = set([root])

        def dfs(node):
            if not node:
                return None

            res = node
            if node.val in to_delete:
                res = None
                result.discard(node)
                if node.left: result.add(node.left)
                if node.right: result.add(node.right)

            node.left = dfs(node.left)
            node.right = dfs(node.right)



            return res

        dfs(root)
        return list(result)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)



solution = Solution()
print(solution.delNodes(root, [3,5]))

