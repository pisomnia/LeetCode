import sys
from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        if not grid or len(grid)==0 or len(grid[0])==0:
            return 0
        res=0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                self.count=0
                self.dfs(grid,i,j)
                res=max(res,self.count)
        return res
    
    def dfs(self,grid,sx,sy):
        if grid[sx][sy]==0:
            return 
        self.count+=1
        grid[sx][sy]=0
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        for d in dirs:
            nx=sx+d[0]
            ny=sy+d[1]
            if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]):
                self.dfs(grid,nx,ny)

        """
        if not grid:
            return
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res=max(res,self.dfs(grid, i, j))                   
        return res
    
    def dfs(self,grid,sx,sy):
        if grid[sx][sy]==0:
            return 0  
        count=1
        grid[sx][sy]=0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in dirs:
            nx=sx+d[0]
            ny=sy+d[1]
            if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]):
                count+=self.dfs(grid,nx,ny)
        return count
        