class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        substring_array = []

        for i in range(0,len(s)-2):
            str1 = s[i]+s[i+1]+s[i+2]
            substring_array.append(str1)

        count = 0

        for substr in substring_array:
            count+=1
            dict1 = {}
            for char in substr:
                if char in dict1:
                    dict1[char] +=1

                else:
                    dict1[char] = 1
            for value in dict1.values():
                if value>=2:
                    count-=1
                    break
        
        return count