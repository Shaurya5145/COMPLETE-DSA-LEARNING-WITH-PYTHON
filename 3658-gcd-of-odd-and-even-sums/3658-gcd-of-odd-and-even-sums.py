class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        sumOdd = n**2
        sumEven = (n*n)+n

        return sumEven-sumOdd