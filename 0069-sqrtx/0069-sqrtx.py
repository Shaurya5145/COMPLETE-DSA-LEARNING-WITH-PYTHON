class Solution:
    def mySqrt(self, x: int) -> int:
        
        ans = 0

        if x==0 or x==1:
            return x

        for i in range(1,x+1):

            if i*i < x:
                continue
            elif i*i>x:
                return i-1
            else:
                return i