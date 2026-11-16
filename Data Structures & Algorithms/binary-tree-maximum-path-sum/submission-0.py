from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with root.val since the path must be non-empty (handles all-negative trees)
        self.max_sum = root.val
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Compute max gain from left and right subtrees; ignore negative paths
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Check the path that splits at the current node (left -> node -> right)
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the best single-branch gain extendable by the parent
            return node.val + max(left_gain, right_gain)
            
        dfs(root)
        return self.max_sum