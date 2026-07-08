class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #so we will have 2 dictionaries , one to contain all the letters of string t
        #which will always be fixed
        #and one to contain the other letters

        #we will first start with saying if string t is empty, then we return an empty string
        if t == "":
            return ""
        
        countT = {}
        window = {}
        #now we make our fixed window(our string t dictionary that never changes)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        #now we have our dictionary full of the letters in t and their values
        have = 0 # the amount of letters we have in our "window" dictionary
        #this is what we will use to compare with need. 
        #need is the number of letters in the constant countT dictionary
        #have is the count of what we have in the window dictionary
        need = len(countT)
        resLength = float("inf")
        res = [-1, -1] # this is where we will keep our pointer values
        #it will end up as [l,r] which shows us the start of the shortest substring and the 
        #end of the shortest substring
        l = 0 # initialize l
        # now lets make our "window" dictionary window and the main sliding window logic
        #th logic is, only shrink the window while our have is = to need
        #cuz if our have == need, it means we have a valid window/a valid substring of s that contains t
        # we can shrink it from the left and still have a valid substring(if lets say one letter appears more than once in the substring)
        #which is why its safest to use a while, instead of if.
        #we will only stop shrinking once have != need, meaning all the letters in t, no longer exist in the 
        #substring of s, so we need to keep expanding our widow to find more(if we still have leter left in s(which our for loop handles))
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # now we have all the letters in s and their values in the dictionary
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLength:
                    res = [l, r]
                    resLength = r - l + 1
                #now we shrink, first we need to decrement the value of the letter we are shrinking in window dictionary
                window[s[l]] -= 1
                #now we decrement have
                # we need to see if the letter we are removing exists in countT dictionary
                #cuz  we only want the letters that are in string t! to affect the have amount
                # we also need to check if the value of the letter is less, cuz if for exaple
                # before decrementing, in the subarray of string s a = 2  (lets say t = abc) after decrementing, a = 1, and a is already 1 in dictionary countT
                #which means that its STILL a valid subarray! cuz that letter still exists
                # so we will only decrement have if a drops down to 0, meaning, it is no longer a valid sub array! therefore we have to decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1 # move l forward
        l,r = res # stroing the final l and r  values in res array
        if resLength == float("inf"):
            return ""
        else:
            return s[l: r+1]  # +1 due do python rules of stopping BEFORE that stop value 
            #if we say l:r itll stop at the letter BEFORE r, we need it to stop AT r, so we do +1

            #space: O(m), timeO(n+m)






        