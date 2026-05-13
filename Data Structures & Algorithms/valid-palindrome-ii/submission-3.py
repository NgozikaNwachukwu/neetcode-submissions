class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
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

        a = 0 # starts at first letter
        b = len(s)-1 # starts at last letter
        while a < b:
            if s[a] != s[b]:
                path_a = isPalindrome(a+1, b)
                path_b = isPalindrome(a, b-1)
                #basically there are 2 paths we can take, if theyre not equal
                # we can say lets skip the letter currently at "a" and continue
                # to check if the rest of the string is a palindrome
                #or we could skib b and check if the rest of the string is a 
                #palindrome
                if path_a or path_b: # if either path a or b worked the answer is true
                    return True
                elif not path_a and not path_b:
                    return False # return false if BOTH paths failed
            a += 1
            b -= 1
        return True

        #time =  approximately O(n) because we are going over each letter once
        # which is n times, even through we will be calling a helper method we are still
        # going over the string n times.
        # space = O(1) still. because space stays constant in this case. there is no extra
        # data structure we are using to store the string, all operations are done in place


            
                

        
        