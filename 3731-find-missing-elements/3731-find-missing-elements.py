class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 2:
            return nums

        min_val = min(nums)
        max_val = max(nums)

        num_set = set(nums)

        missing_integers = []

        for i in range(min_val+1,max_val):
            if i not in num_set:
                missing_integers.append(i)

        return missing_integers