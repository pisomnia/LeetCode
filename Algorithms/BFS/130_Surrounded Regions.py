class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0])==0 or len(board)==0:
            return board
        m=len(board)
        n=len(board[0])
        
        for i in range(m):
            self.bfs(board,i,0)
            self.bfs(board,i,n-1)
            
        for j in range(n):
            self.bfs(board,0,j)
            self.bfs(board,m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='W':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
            
            
    def bfs(self, board, sx, sy):
        if board[sx][sy] !='O':
            return
        queue=[]
        queue.append((sx,sy))
        board[sx][sy]='W'
        while queue:
            cx,cy=queue.pop(0)
            dirc=[(-1,0),(1,0),(0,1),(0,-1)]
            for d in dirc:
                nx=cx+d[0]
                ny=cy+d[1]
                if (nx>=0 and nx<len(board) and ny>=0 and ny<len(board[0]) and board[nx][ny]=='O'):
                    board[nx][ny]='W'
                    queue.append((nx,ny))
