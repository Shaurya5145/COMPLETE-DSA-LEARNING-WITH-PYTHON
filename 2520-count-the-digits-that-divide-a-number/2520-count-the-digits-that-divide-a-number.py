class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        fix_num = num
        while num!=0:
            digit = num%10
            if fix_num%digit==0:
                count+=1
            num//=10
        return count
            
        