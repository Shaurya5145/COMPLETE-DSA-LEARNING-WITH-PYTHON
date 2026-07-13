class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] +=1

        freq2 = {}

        for char in t:
            if char not in freq2:
                freq2[char] = 1
            else:
                freq2[char] +=1

        for char in freq:
            if char in freq2:
                if freq[char] != freq2[char]:
                    return False
            else:
                return False

        if len(s)!=len(t):
            return False

        return True

