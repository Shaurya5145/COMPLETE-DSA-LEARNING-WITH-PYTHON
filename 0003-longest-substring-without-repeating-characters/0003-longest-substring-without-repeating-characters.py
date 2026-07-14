class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0

        ans = 1
        
        dict1 = {s[0]:1}

        i = 0
        j = 1

        while j<len(s):
            while s[j] in dict1:
                del dict1[s[i]]
                i+=1
            dict1[s[j]] = 1
            j+=1
            ans = max(ans,len(dict1))

        return ans

        