# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(node: Optional[TreeNode], d: int):

            if not node:
                return d

            d = max(helper(node.left, d), helper(node.right, d))

            return d + 1

        return helper(root, 0)
        