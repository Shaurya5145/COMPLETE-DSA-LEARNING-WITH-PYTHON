class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0

        end = len(numbers)-1

        sum = numbers[start]+numbers[end]

        while sum!=target:

            sum = numbers[start]+numbers[end]

            if sum<target:
                start+=1
            elif sum>target:
                end-=1

            else:
                return [start+1,end+1]

        return [start+1,end+1]