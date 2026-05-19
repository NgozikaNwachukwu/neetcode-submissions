class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                a = stack.pop() # topmost number
                b = stack.pop() # bottom number
                # it needs to be bottom number - topmost number
                if token == "+":
                    c = b + a
                elif token == "-":
                    c = b - a
                elif token == "*":
                    c = b * a
                elif token == "/":
                    c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(token))

        return stack[-1] # the last memeber in the stack

        
        