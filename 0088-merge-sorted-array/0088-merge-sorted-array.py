class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        g = m
        arr = []

        while i<len(nums1) and j<len(nums2) and g>0:
            if nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i+=1
                g-=1
            else:
                arr.append(nums2[j])
                j+=1

            k+=1

        while i<m:
            arr.append(nums1[i])
            k+=1
            i+=1

        while j<len(nums2):
            arr.append(nums2[j]) 
            k+=1
            j+=1

        nums1[:] = arr

        
            

            
        