class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        operators = {"+", "D", "C"}
        for opp in operations:
            if len(stack) != 0:
                if opp not in operators:
                    stack.append(int(opp))
                    
                    
                elif opp == "+" and stack:
                    a = stack.pop() #topmost
                    b = stack.pop() # last element
                    c = b + a # add them
                    stack.append(b)
                    stack.append(a)
                    stack.append(c)
                elif opp == "C" and stack:
                    stack.pop()
                elif opp == "D" and stack:
                    z = stack.pop()
                    y = z * 2
                    stack.append(z)
                    stack.append(y)
                
            
            else:
                stack.append(int(opp))

        return sum(stack)
        