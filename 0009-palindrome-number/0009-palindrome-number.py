class Solution:
    def isPalindrome(self, x: int) -> bool:
        fix_num = x
        rev = 0
        while x>0:
            digit = x%10
            rev = (rev*10)+digit
            x//=10
        if fix_num==rev:
            return True
        else:
            return False