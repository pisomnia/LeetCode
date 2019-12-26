from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid)==0 or len(grid[0])==0:
            return 0
        res=0         
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                res=max(res,self.bfs(grid,i,j))
        return res
    
    def bfs(self,grid,sx,sy):
        if grid[sx][sy]==0:
            return 0
        count=0
        queue=deque()
        queue.append((sx,sy))
        grid[sx][sy]=0
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            cx,cy=queue.popleft()
            count+=1
            for d in dirs:
                nx=cx+d[0]
                ny=cy+d[1]
                if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and grid[nx][ny]==1:
                    grid[nx][ny]=0
                    queue.append((nx,ny))
        return count
