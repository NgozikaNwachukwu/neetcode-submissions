class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need_map = {}
        for char in s1:
            need_map[char] = 1 + need_map.get(char, 0)

        window_map = {}
        left = 0

        for right in range(len(s2)):
        # Add the incoming character
            char_in = s2[right]
            window_map[char_in] = 1 + window_map.get(char_in, 0)

        # Shrink if the window is too large
            if right - left + 1 > len(s1):
                char_out = s2[left]
                window_map[char_out] -= 1

            # Remove characters with frequency zero cus if need= {a:1, b:1} and window = {a:1, b:1, c:0} we need to delete it
                if window_map[char_out] == 0:
                    del window_map[char_out]

                left += 1

        # Compare the frequencies directly
            if window_map == need_map:
                return True

        return False
