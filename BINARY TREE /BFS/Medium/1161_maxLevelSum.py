from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: [TreeNode]) -> int:

        if not root:
            return 0

        q = deque([root])
        level = []

        while q:
            length = len(q)
            cur_sum = 0
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cur_sum += node.val

            level.append(cur_sum)


        return level.index(max(level)) + 1



root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)


solution = Solution()
count = solution.maxLevelSum(root)
print(count)
