# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy #make a dummy node and mke its pointer prev

    #the list1 and list2 are POINTERS!
        while list1 and list2 is not None:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next # move pointer
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next #move prev pointer

        if list1 is not None:
            prev.next = list1 # if the list1 pointer still is not none, after list2 point becomes none, then just  add the node to list by making prev = next = list1
        elif list2 is not None:
            prev.next = list2 #same thing just append, if the pointer isnt none and list1 is none
            #this is how I understand it anyways, not sure if its right
        return dummy.next


        