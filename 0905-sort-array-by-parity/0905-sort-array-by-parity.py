class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        arr = [0]*(len(nums))
        start = 0
        end = len(nums)-1

        for num in nums:
            if num%2==0:
                arr[start] = num
                start+=1
            else:
                arr[end] = num
                end-=1

        return arr