# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def pre_order(root):
            nonlocal ans
            if root.val >= low and root.val <= high:
                ans += root.val
            if root.left:
                pre_order(root.left)
            if root.right:
                pre_order(root.right)
        pre_order(root)
        return ans