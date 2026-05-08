# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        
        #edge case if the list is empty or has one node return the head
        

        while curr is not None and curr.next is not None:
            last = curr
            prev_last = None

            while last.next is not None:
                prev_last =last #keeping a node before last
                last = last.next #to make sure this resets us to last node
            
            
            if curr.next is None or curr.next == last:
                    break

            prev_last.next = None

            last.next = curr.next
            curr.next = last
            curr = curr.next.next
        
        