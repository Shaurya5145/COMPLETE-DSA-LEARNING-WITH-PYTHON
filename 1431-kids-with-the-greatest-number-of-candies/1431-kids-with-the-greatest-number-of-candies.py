class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        is_greater = False
        max_candies = max(candies)
        bool_array = []
        for candy in candies:
            if candy+extraCandies>=max_candies:
                bool_array.append(True)
            else:
                bool_array.append(False)
        return bool_array            