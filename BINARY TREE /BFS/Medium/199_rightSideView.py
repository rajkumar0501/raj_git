from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: [TreeNode]) -> [int]:

        if not root:
            return []

        r = []
        q = deque([root])


        while q:
            length = len(q)

            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if node == None:
                    node = q.popleft()

            r.append(node.val)


        return r

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)




solution = Solution()
count = solution.rightSideView(root)
print(count)
