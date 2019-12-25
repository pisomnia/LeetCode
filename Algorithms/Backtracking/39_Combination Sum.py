class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(candidates,target,0,[],res)
        return res
    
    def dfs(self,nums,target,start,cur,res):
        if sum(cur)>target:
            return
        if sum(cur)==target:
            res.append(list(cur))
        for i in range(start,len(nums)):
            cur.append(nums[i])
            self.dfs(nums,target,i,cur,res)
            cur.pop()