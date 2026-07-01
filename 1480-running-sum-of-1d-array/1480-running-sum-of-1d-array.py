class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans_list = []
        current_sum = 0

        for num in nums:
            current_sum+=num
            ans_list.append(current_sum)

        return ans_list
            
            

