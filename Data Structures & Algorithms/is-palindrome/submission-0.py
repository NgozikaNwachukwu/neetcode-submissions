class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_trimmed = "".join(c.lower() for c in s if c.isalnum())
        return s_trimmed == s_trimmed[::-1]