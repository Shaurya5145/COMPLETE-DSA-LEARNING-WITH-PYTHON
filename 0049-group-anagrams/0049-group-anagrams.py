class Solution:
    def sortstring(self,s: str):
        s = list(s)
        s.sort()
        return "".join(s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = {}

        for i in strs:
            key = self.sortstring(i)

            if key in dict1:
                dict1[key].append(i)

            else:
                dict1[key] = [i]

        return list(dict1.values())

        
