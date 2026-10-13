class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)# will produce = {"A": 3, "B": 2, "C": 2} for instance
        maxHeap = [-cnt for cnt in count.values()] # will produce a negative array of all the values in the count dictionary

        heapq.heapify(maxHeap) # convert maxHeap list to a heap so that itll be sorted in ascending order (so we will be able to use the max heap efficiently, collecting the largest values first
        time = 0 #initialize time
        q = deque() #initialize our queue (to help us store the remaining count of that letter and the time till we can use it next)

        while q or maxHeap: # keeps going until both maxHeap and queue is empty
            time += 1 #start counting time
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # add one to decrease its remaining frequency
                if cnt != 0: #only add to queue if theres frequencies left
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                remains = q.popleft()[0] #pop out the remaining frequency ONLY
                heapq.heappush(maxHeap, remains)

        return time





        