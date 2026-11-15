# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both nodes are greater than the current node, go right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both nodes are smaller than the current node, go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # We found the split point (LCA)
                return curr