class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #the idea is that we are creating a new list with the index of each of the tasks attached (index in the array) amd sorting them cuz we ned to know which to excecute first
        # we need to make a variable time, whichll be the amount of processing tie so far
        # variable i will be keeping track of the number of tasks we have processed so far, so we stop processing when all the tasks are done
        #if the time is less than the first value in the tuple arrray(which represents the enqued time to process that task) then we make sure time is equal to that enqued number
        #we need an inner while loop to keep adding to the minheap as long as it is eligible to be processed. if time is greater than a tasks enqued time, it means its eligibe to be processed(depending on the processing time since we choose the one with lower processing time and thats what the heap is for to arrage the ones from smaleest processing time to largest)
        #and then move the task forward by the task we just processed and add the index time to the results array

        newTasks = [] # create the new tasks array

        for i, task in enumerate(tasks):
            enqueTime = task[0]
            processTime = task[1]
            newTasks.append((enqueTime, processTime, i)) # add the enque time processing time and the index of this time to the array cuz we need to retun the order of tasks processed
        newTasks.sort() #need to sort is cuz we need to know the one we will process first(has the smallest enque time meaning the cpu will process it first, and the index is added to each task subarray so we actually KNOW the number of the task)

        result = []# storing the order they were processed
        time = 0 #time is keeping track of our enque time
        i = 0 # keeping track of how may taks we have processed so far
        minHeap = [] #create our minheap

        while i < len(tasks) or minHeap:
            if not minHeap and time < newTasks[i][0]:
                time = newTasks[i][0] #so time jumps to our most recent enque time

            while i < len(tasks) and newTasks[i][0] <= time: # this makes sure that this loop does become infinite, if i exceeds the number of tasks it cannot keep adding imaginary tasks to our min heap and most importantly makes sure we add all tasks elligible to be processed by the cpu to the minheap cuz if this task is elligible its enque time will be less than(meanining we already passed the enque time as we were processing the last task) or = to the time(coincidentally the enque time for a task is = where out time is right now)
                enqTime, procTime, index = newTasks[i]
                heapq.heappush(minHeap, (procTime, index)) 
                i += 1 #increment i to ensure we keep track of how many tasks have been processed by cpu and that the while loop has a good end condition
        #now the heap wll arrange the processing time from smallest to largest cuz we need to process tasks that have smaller processng time and the "If multiple tasks have the same shortest processing time, it will choose the task with the smallest index." is handled by heaps too cuz if they both have the same processing time heaps, will arrage based on the next value in the subarray which will be our index so what will be popped out will be obeying the rules
            procTime, index = heapq.heappop(minHeap)
            time += procTime # time should be the next enque time plus our current time

            result.append(index)
        return result










