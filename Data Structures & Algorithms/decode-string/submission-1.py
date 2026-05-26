class Solution:
    def decodeString(self, s: str) -> str:
        # the objective is to add into the stack until we see a closed bracket
        # when we see a closed bracket, we have reached a sub problem
        # so we pop till we get to the open bracket
        # we pop that open bracket, and then pop keep popping to fing the number
        # the number that we will be multpilying it by
        # then we append the multiplied versions
        # then return the joined string
        stack = [] # make the stack
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else: # this is where the doozy starts
                # I will start popping out of the stack till we get to an open bracket
                substr = "" # create an empty string to add the strings we are popping to
                while stack[-1] != "[":
                    substr = stack.pop() + substr # this ensures proper format. 
                    # e.g if stack has cd (d is topmost) subst will first be d, then next
                    # iteration be c + d so it stays cd.
                stack.pop() # pop out the open bracket

                k = "" # where we will collect the number to multiply
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # same logic as substr above
                
                stack.append(int(k) * substr) # YES! in python you can multply strings like this
        final = "".join(stack) # join all the strings
        return final
                    
        