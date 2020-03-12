class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        area=0
        heights=heights+[0]
        for index in range (len(heights)):
            while stack and heights[index]<=heights[stack[-1]]:
                poped_index=stack.pop()
                if stack:
                    width=index-stack[-1]-1
                else:
                    width=index
                area=max(area,width*heights[poped_index])            
            stack.append(index)
        return area
        