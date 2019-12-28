class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or len(digits)==0:
            return []
        self.hashmap={}
        self.hashmap['2']='abc'
        self.hashmap['3']='def'
        self.hashmap['4']='ghi'
        self.hashmap['5']='jkl'
        self.hashmap['6']='mno'
        self.hashmap['7']='pqrs'
        self.hashmap['8']='tuv'
        self.hashmap['9']='wxyz'
        res=[]
        self.dfs(digits,'',res)
        return res
    def dfs(self,digits,path,res):
        if len(path)==len(digits):
            res.append(path)
            return
        for char in self.hashmap[digits[len(path)]]:
            self.dfs(digits,path+char,res)

