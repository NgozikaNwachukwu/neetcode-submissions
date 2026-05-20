class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        l = 0
        result = []
        for i in range(len(temperatures)):
            l = i
            count = 0
            if l + 1 < len(temperatures) and temperatures[l+1] > temperatures[l]:
                count += 1
                result.append(count)
            else:
                while l + 1 < len(temperatures) and temperatures[l+1] <= temperatures[i]:
                    l += 1
                    count += 1
                if l+1 < len(temperatures):
                    count += 1 # counting the warmer day
                else:
                    count = 0
                result.append(count)
        return result


