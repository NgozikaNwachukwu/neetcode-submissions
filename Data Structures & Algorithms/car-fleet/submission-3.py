class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = [] # create stack
        for p, s in cars:
            finish_time = (target - p) / s
            if len(stack) != 0 and finish_time <= stack[-1]:
                continue
            else:
                stack.append(finish_time)
        return len(stack)
        
        