class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        fix_num = n
        sum = 0
        product = 1

        while n>0:
            digit = n%10
            product*=digit
            sum+=digit
            n//=10
        return product-sum