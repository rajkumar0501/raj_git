class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def dfs(node):
            if not node:
                return False

            if node == p or node == q:
                return node


            l = dfs(node.left)
            r = dfs(node.right)


            if l and r:
                return node
            else:
                return l or r


        return dfs(root)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
p = root.left
q = root.left.right.right


solution = Solution()
lowestCommonAncestor = solution.lowestCommonAncestor(root, p, q)
print(lowestCommonAncestor.val)
