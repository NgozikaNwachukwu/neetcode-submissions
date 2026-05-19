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
                    # The problem requires division to "truncate toward zero".
                    # This means we must completely CHOP OFF the decimal part 
                    # without doing any mathematical rounding up or down.
                    #
                    # Python's standard floor division (//) always rounds DOWN
                    # toward negative infinity. This causes bugs with negatives:
                    #   -6 // 11 evaluates to -1 (Python rounds down)
                    #
                    # By using float division (b / a) inside int(), Python 
                    # instantly deletes the decimal point and drops everything 
                    # to the right of it. This perfectly satisfies LeetCode:
                    #   int(-0.5454) drops the decimal and correctly leaves 0.
                    c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(token))

        return stack[-1] # the last memeber in the stack

        
        