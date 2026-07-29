class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        n = len(arr)

        l = 0
        r = n-1
        pk = 0

        while l<=r:
            mid = (l+r)//2

            if arr[mid-1]<arr[mid]:
                if arr[mid+1]<arr[mid]:
                    pk = mid
                    return pk
                else:
                    l = mid+1
            else:
                r = mid
        
        