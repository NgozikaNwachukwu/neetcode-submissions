class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 2. Determine what the new minimum value is.
        # If the min_stack has items, compare the current 'val' with the 
        # previous minimum (which sits at self.min_stack[-1]).
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
        else:
            current_min = val
        
        # 3. Push the calculated minimum onto the min_stack
        self.min_stack.append(current_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
