class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<4 or len(s)>12:
            return []
        res=[]
        self.dfs(s,[],res)
        return res
    
    def dfs(self,s,path ,res):
        if not s and len(path)==4:
            res.append('.'.join(path))
        if not s or len(path)==4:
            return
        for i in range(1,4):
            if len(s)<i:
                continue
            number =int(s[:i])
            if str(number)==s[:i] and number<=255:
                self.dfs(s[i:],path+[s[:i]],res)
