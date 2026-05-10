class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if its even we need to stop once l>r
        #if its odd we stop once l=r
        l = 0 # starts at first letter
        r = len(s)-1 # starts at last letter
        while l < r: # if l becomes = r or l > r we stop
            if not s[l].isalnum():
                l += 1
                continue # this ensures that we go BACK to the top of the loop to check if 
                #the new l we have moved to is also alphanumeric. eg if s =", , a"
                #itll try to compare space to a which will cause a crash!
            elif not s[r].isalnum():
                r -= 1 
                continue # same thing, loop goes back to beginning to ensure the new r
                # we are on is alphanumeric
            
            if s[l].lower() == s[r].lower(): #python is very strict with comparisons!
            # A =! a in pyhton. so we need to lower before we check!
                l += 1
                r -= 1
            else:
                return False

        return True

        