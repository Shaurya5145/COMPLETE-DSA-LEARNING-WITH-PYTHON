class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}

        for i in s:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] = 1

        charcter1 = None

        print(dict1)

        for (key,value) in dict1.items():
            if value==1:
                character1 = key
                break

        if 1 in list(dict1.values()):
            return s.find(character1)
        return -1

