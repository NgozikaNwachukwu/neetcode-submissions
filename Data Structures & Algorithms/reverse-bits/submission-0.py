class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        reversed_n = binary[::-1]
        decimal = int(reversed_n, 2)

        return decimal