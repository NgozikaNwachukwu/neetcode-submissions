class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
    # 1. Base case check
        if len(s1) > len(s2):
            return False

    # 2. Build the 'need' dictionary (s1 frequency map)
        need_map = {}
        for char in s1:
            need_map[char] = 1 + need_map.get(char, 0)
        
        need = len(need_map) # Number of unique characters that need to match
        have = 0             # Number of unique characters currently matching the target count
    
    # 3. Initialize the 'have' window dictionary
        window_map = {}
    
    # 4. Slide the window across s2
        left = 0
        for right in range(len(s2)):
        # Add the incoming character to the window
            char_in = s2[right]
            window_map[char_in] = 1 + window_map.get(char_in, 0)
        
        
            if char_in in need_map:
                if window_map[char_in] == need_map[char_in]:
                    have += 1
                elif window_map[char_in] == need_map[char_in] + 1:
                    have -= 1
            
        # Your logic: If the window size exceeds len(s1), shrink it from the left
            if (right - left + 1) > len(s1):
                char_out = s2[left]
            
            # Decrement the letter count at the left pointer first
                window_map[char_out] -= 1
            
            # Check if this drop caused the window count to fall below what s1 requires
                if char_out in need_map:
                    if window_map[char_out] == need_map[char_out]:
                        have += 1
                    elif window_map[char_out] == need_map[char_out] - 1:
                        have -= 1
                
                left += 1
            
        # Check if the current window is a perfect match
            if have == need:
                return True
            
        return False
