class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #optimized using a monotonic stack
        result = [0] * len(temperatures) # Start with an answer list filled with 0s.
        stack = [] #This stack will ONLY store day indexes (e.g., [0, 1, 2...])
        for current_day in range(len(temperatures)):
            # 4. Check if the waiting room (stack) has days in it, AND if the 
            # current day's temperature is WARMER than the day at the top of the stack.
            while stack and temperatures[current_day] > temperatures[stack[-1]]:
                past_day = stack.pop() # Pop the older day out of the waiting room
                # The wait time is simply: Current Day Index - Past Day Index
                result[past_day] = current_day - past_day

            stack.append(current_day)# append the index of the current day onto the stack if otherwise
        return result
       

