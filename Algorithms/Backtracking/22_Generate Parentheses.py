class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res=[]
        left=0
        right=0
        self.dfs(left,right,'',res,n)
        return res
        
    def dfs(self,left,right,path,res,n):
        if right>left:
            return
        if len(path)==2*n:
            res.append(path)
            return
        if left <n:
            self.dfs(left+1,right,path+'(',res,n)
        if right<n:
            self.dfs(left,right+1,path+')',res,n)