# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = head
        prev = dummy
        for _ in range(n):
            curr = curr.next
        start = head
        while curr:
            curr = curr.next
            prev = start
            start = start.next
        
        prev.next = start.next
        
        return dummy.next