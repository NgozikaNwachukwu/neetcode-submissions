class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(0, n+1):
            binary = bin(i)[2:]
            ones = binary.count('1')
            answer.append(ones)
        
        return answer
        