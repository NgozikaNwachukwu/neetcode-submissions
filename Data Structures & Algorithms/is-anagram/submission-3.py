class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the lengths are even equal to start 
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # 2. THE SORTING (O(n log n) Time)
        # Python's sorted() takes s and t and creates TWO new lists.
        # Even though we do it twice (n log n + n log n), we drop 
        # the constant '2', so the time complexity is O(n log n).
        
        # 3. THE COMPARISON (O(n) Time)
        # Comparing two lists with '==' means Python walks through 
        # both lists to check every character.
        
        # FINAL COMPLEXITY:
        # TIME: O(n log n) 
        # (Because the sorting is the "heaviest" part of the code).
        
        # SPACE: O(n)
        # Why? Because sorted() does NOT change the original string.
        # It builds a brand-new list in memory to hold the characters.
        # If the string has 'n' letters, you need 'n' space for the new list.