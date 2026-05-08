# Definition for singly-linked list.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #make a dummy node
        #point that dummy node to head
        #make a pointer called prev that points to dummy
        #make a pointer current that points to prev.next
        #make a next pointer probs in the loop
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current.next is not None:
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next

        