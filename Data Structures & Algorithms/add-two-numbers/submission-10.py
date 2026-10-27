# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        carry = False
        curr = dummy
        while l1 and l2:
            total = l1.val + l2.val
            if carry:
                total += 1
            if total < 10:
                carry = False
            elif total >= 10:
                carry = True
            total = total % 10
            node = ListNode(val=total)
            curr.next = node

            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            if carry:
                l1.val += 1
            if l1.val < 10:
                carry = False
            l1.val = l1.val % 10
            node = ListNode(val=l1.val)
            l1 = l1.next
            curr.next = node
            curr = curr.next
                

        while l2:
            if carry:
                l2.val += 1
            if l2.val < 10:
                carry = False
            l2.val = l2.val % 10
            node = ListNode(val=l2.val)
            l2 = l2.next
            curr.next = node
            curr = curr.next
        
        if carry:
            curr.next = ListNode(val=1)

            
        return dummy.next