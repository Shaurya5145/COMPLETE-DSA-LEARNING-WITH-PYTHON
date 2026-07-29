class Solution:
    def lowerBound(self,nums,target):

        n = len(nums)
        l = 0
        r = n-1
        lb = n

        while l<=r:
            mid = (l+r)//2

            if nums[mid]>=target:
                lb = mid
                r = mid-1

            else:
                l = mid+1

        return lb

    def upperBound(self,nums,target):

        n = len(nums)
        l = 0
        r = n-1
        ub = n

        while l<=r:
            mid = (l+r)//2

            if nums[mid]>target:
                ub = mid
                r = mid-1

            else:
                l = mid+1

        return ub

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lb = self.lowerBound(nums,target)
        ub = self.upperBound(nums,target)

        if lb==ub:
            return [-1,-1]

        print(lb,ub)

        return [lb,ub-1]

        
