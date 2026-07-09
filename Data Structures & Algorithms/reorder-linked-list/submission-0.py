# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
       
        curr = second
        prev = None
        nex = None

        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            

        reversedList = prev
        
        curr1 = head
        curr2 = reversedList

        while curr2 is not None:
            nex1 = curr1.next
            nex2 = curr2.next

            curr1.next = curr2
            curr2.next = nex1

            curr1 = nex1
            curr2 = nex2
        
        return None

