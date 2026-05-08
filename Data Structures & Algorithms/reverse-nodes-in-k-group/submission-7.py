class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head
        dummy = ListNode(0) #make a dummy nodd
        dummy.next = head # make it point to the head
        prev = dummy # pointer that points to dummy, this will help wity first reversal
        #three pointers, temp, mid, prev. temp = mid.next, temp.next =prev.next, prev.next =temp
        curr = head
        while curr is not None:
            group_head = curr
            counter = 1 
            while curr.next and counter < k:
                curr = curr.next
                counter += 1# we need to put this in this while loop! so it can actually reset
                #print(counter)

            if counter == k:
                #print(counter)
                next_node = curr.next 
                mid = prev.next
                for _ in range(k-1):
                    temp = mid.next
                    mid.next = temp.next
                    temp.next = prev.next
                    prev.next = temp
                    #print(temp)
                prev = group_head
                curr = next_node
            if counter < k: #if counter < k or >k
                break
        #print(dummy.next.val)
        return dummy.next