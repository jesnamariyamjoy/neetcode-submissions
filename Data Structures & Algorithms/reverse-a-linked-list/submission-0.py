# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next     # Temporarily store the next node
            curr.next = prev    # Reverse the current node's pointer
            prev = curr         # Move prev forward
            curr = nxt          # Move curr forward
            
        return prev             # prev is the new head of the reversed list