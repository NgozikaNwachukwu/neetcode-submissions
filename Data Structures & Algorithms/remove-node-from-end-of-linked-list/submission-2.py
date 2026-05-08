# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy 
        fast = dummy 
        if head is None or head.next is None :
            return None
        #we initialize fast and slow to dummy
        counter = 0
        while counter < n:
            fast = fast.next 
            counter += 1
        while fast.next is not None:
            slow = slow.next
            fast = fast.next 
        slow.next = slow.next.next
        return dummy.next





        