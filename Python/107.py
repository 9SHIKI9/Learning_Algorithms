# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            tmp = []
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(tmp)
        return res[::-1]
