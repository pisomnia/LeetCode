##Backtracking use visited matrix consverse the global state
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word=="":
            return True
        if not board or len(board[0])==0:
            return False
        m=len(board)
        n=len(board[0])
        visited=[[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board,word,visited,i,j,0):
                    return True
        return False
    
    def dfs(self,board,word,visited,row,col,k):
        if k==len(word):
            return True
        m=len(board)
        n=len(board[0])
        if row<0 or row>=m or col<0 or col>=n:
            return False
        if word[k]==board[row][col] and visited[row][col]==False:
            visited[row][col]=True
            if self.dfs(board,word,visited,row-1,col,k+1) or self.dfs(board,word,visited,row+1,col,k+1) or self.dfs(board,word,visited,row,col+1,k+1) or self.dfs(board,word,visited,row,col-1,k+1):
                return True
            visited[row][col]=False
        return False