class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_array = [0]*n
        even_index = 0
        odd_index = n-1

        for i in range(0,n):
            if nums[i]%2==0:
                ans_array[even_index] = nums[i]
                even_index+=1

            else:
                ans_array[odd_index] = nums[i]
                odd_index-=1
        
        return ans_array