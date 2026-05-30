class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        stack1 = []
        stack2 = []
        stack3 = []

        arr1 = list(word1) # [a,b]
        arr2 = list(word2) # [a,b,b,x,x,c]
        while len(arr1) != 0:
            a = arr1.pop()
            stack1.append(a) # at the end will be [b,a]
        
        while len(arr2) != 0:
            b = arr2.pop()
            stack2.append(b) # at the end will be [c,x,x,b,b,a]

        while len(stack1) != 0 or len(stack2) != 0:
            if len(stack1) != 0 and len(stack2) != 0:
                c = stack1.pop()
                d = stack2.pop()
                stack3.append(c)
                stack3.append(d)
            elif len(stack1) == 0 and len(stack2) != 0:
                stack3.append(stack2.pop())
            elif len(stack1) != 0 and len(stack2) == 0:
                stack3.append(stack1.pop())
        
        return "".join(stack3)
        