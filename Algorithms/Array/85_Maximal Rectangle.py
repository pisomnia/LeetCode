class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        max_rectangle=0
        heights=[0]*len(matrix[0])
        for row in matrix:
            for index,num in enumerate(row):
                if num=='1':
                    heights[index]+=1
                else:
                    heights[index]=0
            max_rectangle=max(max_rectangle,self.helper(heights))
        return max_rectangle
    
    def helper(self,heights):
        stack=[]
        res=0
        for i,height in enumerate(heights+[0]):     
            while stack and height<=heights[stack[-1]]:
                poped_index=stack.pop()
                if stack:
                    res=max(res,heights[poped_index]*(i-stack[-1]-1))
                else:
                    res=max(res,heights[poped_index]*i)
            stack.append(i)
        return res