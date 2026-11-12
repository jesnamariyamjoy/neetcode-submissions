# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # Traverse while fast and its next node exist to prevent null pointer exceptions
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True
                
        # If the loop finishes, fast reached the end, meaning no cycle exists
        return False