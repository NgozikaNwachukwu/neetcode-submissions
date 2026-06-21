class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #making our window a set
        # when we add a letter we increase our window size
        # when we remove from the left end we are reducing our window length
        window = set()
        l = 0
        windowLength = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l]) #remove the letter in l's position
                l += 1

            window.add(s[r])
            windowLength = max(windowLength, len(window))

        return windowLength
                

        