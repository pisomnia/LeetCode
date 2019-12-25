class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[j]-nums[j-1]==1:
                    j+=1
                else:
                    break
            if (j-i)==1:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i])+'->'+str(nums[j-1]))
            i=j
        return res