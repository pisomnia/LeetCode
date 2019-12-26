class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
       
        if len(matrix) == 0 or len(matrix[0])==0:
            return False
            
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True
        
        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True
        return False
        """
        if len(matrix) == 0 or len(matrix[0])==0:
            return False
            
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start <= end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y]==target:
                return True
            elif matrix[x][y] < target:
                start = mid+1
            else:
                end = mid-1        
        return False