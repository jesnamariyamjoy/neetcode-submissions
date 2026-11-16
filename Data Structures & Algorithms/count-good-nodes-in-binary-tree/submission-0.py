class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # Current node is good if it is >= the max value seen on this path
            res = 1 if node.val >= max_val else 0
            
            # Update the running maximum for child paths
            new_max = max(max_val, node.val)
            
            # Accumulate good nodes from left and right subtrees
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)
            
            return res
            
        return dfs(root, root.val)