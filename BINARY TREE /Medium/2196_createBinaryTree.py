class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: [[int]]) -> [TreeNode]:

        hash_map = {}
        p = {}

        for x, y, _ in descriptions:
            if x not in hash_map:
                hash_map[x] = TreeNode(x)
            if y not in hash_map:
                hash_map[y] = TreeNode(y)


        for a, b, isLeft in descriptions:
            p[b] = True

            if isLeft:
                hash_map[a].left = hash_map[b]
            else:
                hash_map[a].right = hash_map[b]


        root = None
        for j in hash_map.keys():
            if j not in p:
                root = hash_map[j]


        return root



solution = Solution()
print(solution.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))
