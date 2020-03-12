class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1=len(nums1)
        n2=len(nums2)
        left=self.getKth(nums1,0,nums2,0,(n1+n2+1)/2)
        right=self.getKth(nums1,0,nums2,0,(n1+n2+2)/2)
        return  0.5*(left+right)
    
    def getKth(self,nums1,start1,nums2,start2,k):
        if start1>=len(nums1):
            return nums2[start2+k-1]
        if start2>=len(nums2):
            return nums1[start1+k-1]
        if k==1:
            return min(nums1[start1],nums2[start2])
        m=k/2
        i=start1+min(len(nums1)-start1,m)-1
        j=start2+min(len(nums2)-start2,m)-1
        if nums1[i]>nums2[j]:
            return self.getKth(nums1,start1,nums2,j+1,k-min(len(nums2)-start2,m))
        else:
            return self.getKth(nums1,i+1,nums2,start2,k-min(len(nums1)-start1,m))