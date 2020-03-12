from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or len(rooms[0])==0:
            return rooms
        m=len(rooms)
        n=len(rooms[0])
        queue=deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    queue.append((i,j))
        empty =  2**31-1  
        while queue:
            cx,cy=queue.popleft()
            dirc=[(-1,0),(1,0),(0,1),(0,-1)]
            for d in dirc:
                nx=cx+d[0]
                ny=cy+d[1]
                if nx>=0 and nx<m and ny>=0 and ny<n and rooms[nx][ny]==empty:
                    rooms[nx][ny]=rooms[cx][cy]+1
                    queue.append((nx,ny))
        return rooms