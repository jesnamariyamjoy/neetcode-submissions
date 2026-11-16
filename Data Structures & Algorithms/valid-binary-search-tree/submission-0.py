from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            
            # Current node must strictly lie between low and high
            if not (low < node.val < high):
                return False
            
            # Left subtree must be < node.val; right subtree must be > node.val
            return (valid(node.left, low, node.val) and 
                    valid(node.right, node.val, high))
            
        return valid(root, float("-inf"), float("inf"))