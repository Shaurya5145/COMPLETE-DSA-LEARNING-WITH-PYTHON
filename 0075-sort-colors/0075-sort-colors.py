class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3

        for i in nums:
            freq[i] += 1

        nums.clear()

        for i in range(len(freq)):
            while freq[i]>0:
                nums.append(i)
                freq[i]-=1

        
        