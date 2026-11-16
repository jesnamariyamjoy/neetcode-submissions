from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) root lookup
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            # Base case: empty subtree range
            if left > right:
                return None
            
            # Pick the current root from preorder and advance the pointer
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Split inorder into left and right subtrees around root_val
            mid = inorder_idx[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            
            return root
            
        return dfs(0, len(inorder) - 1)