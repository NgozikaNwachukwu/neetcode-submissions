class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #idea iterate through list, add each number to the minheap, keep the min heap of size k, if minheap size exceedes k, we remove the smallest, until we get to the end, and the two smallest we will take the minimum(since its the kth largest)
        minHeap = [] #start the heap as a list

        for num in nums:
            heapq.heappush(minHeap, num) # add each number to min heap

            if len(minHeap) > k:
                heapq.heappop(minHeap) # pop it(remeber due to min heap property python pops the smallest value out) but we arent storing it anywhere so python does garbage collection
        return minHeap[0] #instead of taking the min of whats currently in the k-sized heap we just return the first value of it(since heap propertly allows python to arrange it in sorted order)

        # OVERALL TIME COMPLEXITY: O(n log k)
        # The loop runs n times.
        # Each iteration performs O(log k) heap operations.
        # Therefore: O(n * log k).

        # OVERALL SPACE COMPLEXITY: O(k)
        # The heap stores at most k+1 elements.
        # No other data structure grows with the input size.