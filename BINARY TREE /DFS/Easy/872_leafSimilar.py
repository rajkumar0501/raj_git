class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:

        def dfs(r, l):
            if not r:
                return

            if not r.left and not r.right:
                l.append(r.val)
                return
            dfs(r.left, l)
            dfs(r.right, l)



        l1 = []
        l2 = []

        dfs(root1, l1)
        dfs(root2, l2)

        return l1 == l2






root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)



solution = Solution()
max_depth = solution.leafSimilar(root1, root2)
print(max_depth)
