from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)] 
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        queue, count = deque([]), 0
        
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        path = []
        while queue:
            node = queue.popleft()
            count+=1
            path.append(node)

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        if count == numCourses:
            return path
        return []