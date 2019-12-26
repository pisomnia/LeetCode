## Binary Search
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # write your code here
        start = matrix[0][0] 
        end = matrix[-1][-1]
        
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.get_num_less_equal(matrix, mid) < k:
                start = mid 
            else:
                end = mid 
        if self.get_num_less_equal(matrix, start) >= k:
            return start
        return end         
            
    def get_num_less_equal(self, matrix, mid):
        m = len(matrix)
        n = len(matrix[0])
        i = 0 
        j = n - 1
        count = 0
        while i < m and j >= 0:
            if matrix[i][j] <= mid:
                i += 1 
                count += j + 1 
            else:
                j -= 1 
        return count


## Heap
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        heap =[(matrix[0][y],0,y) for y in range(len(matrix[0]))]
        heapq.heapify(heap)
        res=0
        for i in range(k):
            res,x,y=heapq.heappop(heap)
            if (x+1)< len(matrix):
                heapq.heappush(heap,matrix[x+1][y])
        return res