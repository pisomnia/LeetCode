class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,0,[],res)
        return res
    
    def dfs(self,nums,start,cur,res):
        if len(cur)>len(nums):
            return
        res.append(list(cur))
        for i in range(start,len(nums)):
            cur.append(nums[i])
            self.dfs(nums,i+1,cur,res)
            cur.pop()