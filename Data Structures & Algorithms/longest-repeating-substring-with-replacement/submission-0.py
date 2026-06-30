class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #the whole idea of this problem(to the best of my understanding)
        #we dont actually need to MANUALLY replace the letters
        #what we are lookig for is the longest substring if we replace the letters
        #so we use a sliding window:
        #we initialize the left and right pointers at the beginning
        #a valid window is if we subtract the length of our current window 
        #by the most frequent letter, and if the resulting number is < or = k
        #then our window is valid.
        #to be able to know the most frequent letter, we keep count of each of the letters
        #in a dictionary.
        #so we scan the dictionary and check for the most frequent value
        #and subtract it fro the current length of our window. its only when the resulting value
        #is < or = k that the window is valid.
        #the resulting number in reality is the number of letters we can replace(number of replacements)
        #with another letter(for example the most frequent letter) to make the longest substring 
        #of matching letters
        #for example if we have ABBABBA, lets say l is at index 0, and r is at index 2
        #the most frequent letter is B(2), and our window size is 3, so if k = 2, 3-2 = 1 and 1 <= k
        # meaning yes we can replace 1 letter(the least frequent which is A) with B, so have a substring of 3
        # so we will store the current length of our window as long as that condition is met
        #int a variable called res
        #and we will be usig a dictionary to keep count of the letters(their frequencies)
        #if the number of replacements is > k, then our window will start shrinking
        #meaning we will move the l pointer forward, and decrement the count of the letter we just left
        #in the dictionary. for example, if we are still using or ABBABBA string above
        # lets say our windw is no longer valid, we need to move l from index 0 to index 1
        # so since we are moving l from a TO b, WE ARE REMOVING THE FIRST A from our window
        # therefore we need to decrement its value in the dictionary. cuz the count is keeing track
        #of the frequency of letters INSIDE OUR WINDOW. and since we are taking a max of the values(to find the most frequent letter's value)
        #this will allow us to have an accurate max
        #cuz think about it, k is the amount of times we are allowed to make replacements right?
        # if our number of replacements is GREATER than k, then our window is invalid cuz we are
        #no longer obeying the rules of the question
        #this is the best way i understad this problem
        count = {}
        res = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            #best way i understand to add values to a dictionary
            # could do: count[s[r]] = 1 + count.get(s[r], 0)
            #which means the value is going to be 1 plus whatever is currently the value(incrementing)
            #if the key doesnt exist in the dictionary, we automatically return 0

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 #decrement the value of the letter in l's position in the dictionary
                l += 1 # move l forward

            res = max(res, r-l+1) # storing the length of the window as long as its valid
            #aka as long as the window - the most frequent letter(max value)(number of replacements) <= k
        return res
        


        