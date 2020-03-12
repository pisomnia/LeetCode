from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
        islands=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!='0':
                    self.bfs(grid,i,j)
                    islands+=1
        return islands
    
    def bfs(self,grid,sx,sy):
        if grid[sx][sy]=='0':
            return
        queue=[]
        queue.append((sx,sy))
        dirc=[(-1,0),(1,0),(0,1),(0,-1)]
        while queue:
            cx,cy=queue.pop(0)
            for d in dirc:
                nx=cx+d[0]
                ny=cy+d[1]
                if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and grid[nx][ny]=='1':
                    grid[nx][ny]='0'
                    queue.append((nx,ny))
