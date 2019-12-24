class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        mark die  ---> live -1
        mark live ---> die 2
        """
        if not board or len(board)==0:
            return
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    lives=self.count(board,i,j)
                    if lives==3:
                        board[i][j]=-1
                if board[i][j] == 1:
                    lives=self.count(board,i,j)
                    if lives<2 or lives>3:
                        board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j] ==-1:
                    board[i][j]=1
                if board[i][j]==2:
                    board[i][j]=0
    def count(self,board,i,j):
        dir=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        res=0
        for d in dir:
            nx=i+d[0]
            ny=j+d[1]
            if nx>=0 and nx<len(board) and ny>=0 and ny<len(board[0]):
                if board[nx][ny]==1 or board[nx][ny]==2:
                    res+=1
        return res