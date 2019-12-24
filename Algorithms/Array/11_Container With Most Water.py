class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        res=0
        while left<right:
            if height[left]<=height[right]:
                area=height[left]*(right-left)
                left+=1
            else:
                area=height[right]*(right-left)
                right-=1
            res=max(res,area)
        return res