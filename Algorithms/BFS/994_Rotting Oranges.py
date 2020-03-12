class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R=len(grid)
        C=len(grid[0])
        fresh=0
        queue=collections.deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i,j))
        if fresh==0:
            return 0
        time=0
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            for i in range(len(queue)):
                sx,sy=queue.popleft()
                for d in dirs:
                    nx=sx+d[0]
                    ny=sy+d[1]
                    if nx<0 or nx>=R or ny<0 or ny>=C or grid[nx][ny]!=1:
                        continue
                    grid[nx][ny]=2
                    fresh-=1
                    queue.append((nx,ny))
            time+=1
        if fresh!=0:
            return -1
        return (time-1)
