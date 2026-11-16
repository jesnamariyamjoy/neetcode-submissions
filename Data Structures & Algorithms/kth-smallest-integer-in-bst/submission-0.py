from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # Drill down to the smallest unvisited node on the left
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            k -= 1
            
            # Return immediately once the k-th smallest node is popped
            if k == 0:
                return curr.val
                
            # Move to the right subtree
            curr = curr.right