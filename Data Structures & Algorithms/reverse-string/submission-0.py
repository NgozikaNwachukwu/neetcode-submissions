class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i, r):
            temp = s[i] # store in a temporary variable
            s[i] = s[r] # put the contents of r into i!
            s[r] = temp # now make r the temporarilt stored variable

        l= 0
        r = len(s) -1
        #initialize 2 points, one at the beginning one at the end
        while l < r:
            if len(s) != 0:
                swap(l, r)
                l += 1
                r -= 1

