class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1 #return one once we have gotten to the end and we start checking from backwards and if we reach here it means this string is valid to decode
            
            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]

            count = dfs(i+1) #we can decode 1 letter from this index

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                count += dfs(i+2) #we can decode 2 letter from this index onwards

            memo[i] = count
            return count

        return dfs(0)

    # Time: O(n) - Memoization ensures each index is fully calculated only once.
# Repeated recursive calls use stored results in O(1) time.

# Space: O(n) - The recursion stack can grow to O(n) depth,
# and the memo dictionary stores up to O(n) results.

# Edge case: s = "231"
#
# At index 0:
# - "2" is valid -> dfs(1)
# - "23" is valid -> dfs(2)
#
# At index 1:
# - "3" is valid -> dfs(2)
# - "31" is INVALID because 31 > 26
# - We skip the two-digit option, but can still decode "3" and "1" separately.
#
# At index 2:
# - "1" is valid -> dfs(3)
# - dfs(3) returns 1 because we reached the end successfully.
#
# Valid decodings:
# 1. "2|3|1" -> BCA
# 2. "23|1"  -> WA
#
# Invalid grouping:
# "2|31" -> 31 is greater than 26.
#
# memo[2] = 1
# memo[1] = 1
# memo[0] = 2
#
# Final answer: 2
#
# IMPORTANT: An invalid two-digit grouping doesn't make the
# entire string invalid. We simply skip that grouping.
        