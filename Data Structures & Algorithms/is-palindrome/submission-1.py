class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if its even we need to stop once l>r
        #if its odd we stop once l=r
        l = 0
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1 
                continue
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

        