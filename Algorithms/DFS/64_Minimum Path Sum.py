import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        if m<=0 or n<=0:
            return
        self.res=sys.maxsize
        visited=[[False for i in range(n)] for j in range(m)]
        visited[0][0]=True
        self.dfs(grid,0,0,visited,0)
        return self.res
        
        
    def dfs(self,grid,sx,sy,visited,count):
        count+=grid[sx][sy]
        if sx==len(grid)-1 and sy==len(grid[0])-1:
            self.res=min(self.res,count)
        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        for d in dir:
            nx=sx+d[0]
            ny=sy+d[1]
            if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and not visited[nx][ny]:
                visited[nx][ny]=True
                self.dfs(grid,nx,ny,visited,count)
                visited[nx][ny]=False
