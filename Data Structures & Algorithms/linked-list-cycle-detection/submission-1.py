# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # initia;ize slow pointer to head
        fast = head # initialize fast pointer to head
        while fast is not None and fast.next is not None:
            slow = slow.next #move slow forard by 1
            fast = fast.next.next # move fast forward by 2
            # if there is a cycle, eventually, after some amount of iterations of the loop
            # fast should be equal to the same node as slow
            if fast == slow:
                return True
        return False

        #DID THIS COMPLETELY MYSELF IN FIRST ATTEMPT!
        