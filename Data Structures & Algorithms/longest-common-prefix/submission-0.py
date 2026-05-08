class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We use the FIRST word as our "Template". 
        # We will check its letters one by one against everyone else.
        # strs[0] is "flow". len("flow") is 4.
        for i in range(len(strs[0])): # i is iterating through each letter in the first word in strs array
            for s in strs: # for every word in the strs array
            # This loop now visits every word to check index 'i'
                
                # --- Step 1: Check for a "STOP" condition ---
                # A) i == len(s): Is the current word too short to have index i?
                # B) s[i] != strs[0][i]: Does this word's letter match our template
                if i == len(s) or s[i] != strs[0][i]:
                    # If TRACE is at i=2:
                    # s is "flight". s[2] is 'i'.
                    # strs[0][2] is 'o'.
                    # 'i' != 'o' -> TRAP TRIGGERS!
                    return s[:i] # return all the letters RIGHT BEFORE i
                     # --- Step 2: If no stop, move to the next word 's' ---
                # i=0: "flow" ok -> "flower" ok -> "flight" ok
                # i=1: "flow" ok -> "flower" ok -> "flight" ok
                # i=2: "flow" ok -> "flower" ok -> "flight" FAIL (return "fl")

            # --- Step 3: All words matched at index i! ---
            # Now the outer loop 'i' increments to the next column.
            
        # If we check every letter of "flow" and never triggered the 'if',
        # then "flow" itself is the common prefix.
        return strs[0] # if not we return the whole first string, cuz that means this is the longest prefix
        