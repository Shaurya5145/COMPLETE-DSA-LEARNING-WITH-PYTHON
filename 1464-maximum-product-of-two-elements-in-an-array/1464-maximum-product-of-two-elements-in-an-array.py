class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max1 = max(nums)
        index = None

        for i in range(len(nums)):
            if nums[i] == max1:
                index = i
                break

        nums.pop(index)
        max2 = max(nums)

        return (max1-1)*(max2-1)