# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None  # Cut the list into two halves
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # Step 3: Merge the two halves alternately
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2