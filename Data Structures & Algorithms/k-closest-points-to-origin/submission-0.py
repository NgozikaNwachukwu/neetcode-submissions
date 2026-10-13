import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #whole idea, use a minheap (start as a list then convert to a heap using heapify function in python)

        #we have to calculate the distance, add it to the heap(before converting to a heap), pop the values out and append the co-ordinates to the final list. 

        #we are popping out the k closest co-ordinate values? how do we know the co-ordinated we are adding to the final list are the closest though? like smallest in distance? due to the minHeap property!! it sorts the list for u in ascending order :) so what we are adding to final is the smallest distance co-ordinates(we added the distance into the coordinate subaray because we wanted the min heap to properly sort it)

        minHeap = [] #creat a min heap first as a list

        for x, y in points: #iterate through points list
            dist = math.sqrt((x ** 2) + (y ** 2)) # calculate distance x^2 + y^2
            minHeap.append([dist, x, y])
            # at the end we will have a list with the distance of each of the coordinates in it

        heapq.heapify(minHeap) #turn it into a heap
        final = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap) # pop out of heap
            final.append([x, y])
            k -= 1 #decrement k! very important (so the while loop runs k times)

        return final
        
        