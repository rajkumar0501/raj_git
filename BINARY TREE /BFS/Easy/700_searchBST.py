from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: [TreeNode], val: int) -> [TreeNode]:

        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                if node.val == val:
                    return node
                if val < node.val:
                    q.append(node.left)
                elif val > node.val:
                    q.append(node.right)


        return None


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


solution = Solution()
count = solution.searchBST(root, 2)
print(count.val)
