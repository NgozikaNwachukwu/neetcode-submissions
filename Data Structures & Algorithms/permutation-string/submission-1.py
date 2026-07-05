class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # --- PREPARATION STEP ---
        # If s1 is longer than s2, s2 cannot possibly contain a permutation of s1.
        # Example: s1 = "goodbye" (7), s2 = "hi" (2). "hi" can't hold a 7-letter anagram.
        if len(s1) > len(s2):
            return False

        # Create two lists of 26 zeros. Each index represents a letter from 'a' to 'z'.
        # Index 0 = 'a', Index 1 = 'b', Index 2 = 'c' ... Index 25 = 'z'.
        # This takes O(1) constant space because the size is always fixed at 26.
        s1Count = [0] * 26
        s2Count = [0] * 26

        # --- FILLING THE INITIAL WINDOW ---
        # Loop through s1 to build our target letter counts, and count the first window of s2.
        # Example: If s1 = "ab", this loops exactly twice (i = 0, then i = 1).
        for i in range(len(s1)):
            # ord() converts a letter into its computer ID number (e.g., ord('a') is 97).
            # Subtracting ord('a') maps that ID directly to a list index from 0 to 25.
            # Example: For 'c', ord('c') - ord('a') -> 99 - 97 = Index 2.
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        # --- IMMEDIATE CHECK ---
        # If the first few letters of s2 are already an exact anagram of s1, we stop immediately.
        # Python allows direct list comparison (s1Count == s2Count checks all 26 slots).
        if s1Count == s2Count:
            return True

        # --- SLIDING WINDOW STEP ---
        # Initialize the left pointer (l) at the very beginning of s2 (index 0).
        l = 0

        # The right pointer (r) starts right after our initial window and slides to the end of s2.
        # Example: If s1 = "ab" (len 2) and s2 = "leab", r starts at index 2 (the letter 'a').
        for r in range(len(s1), len(s2)):

            # 1. ADD THE NEW RIGHT CHARACTER
            # Find the alphabet index for the character entering the window on the right side.
            # Increment its count in s2Count because it is now inside our sliding window.
            s2Count[ord(s2[r]) - ord("a")] += 1

            # 2. REMOVE THE OLD LEFT CHARACTER
            # Find the alphabet index for the character dropping out of the window on the left side.
            # Decrement its count in s2Count because it is no longer inside our sliding window.
            s2Count[ord(s2[l]) - ord("a")] -= 1

            # 3. SHIFT THE LEFT POINTER
            # Move the left pointer forward by 1 to keep the window size perfectly stable.
            l += 1

            # 4. CHECK FOR SUCCESS
            # Check if our newly updated window matches the target letter counts perfectly.
            if s1Count == s2Count:
                return True

        # If the loop finishes without finding a match, no valid permutation exists.
        return False
