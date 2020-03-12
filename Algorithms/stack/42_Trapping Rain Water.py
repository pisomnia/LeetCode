class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[]
        ans=0
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                top=stack.pop()
                if stack:
                    distance=i-stack[-1]-1
                    h=min(height[i],height[stack[-1]])-height[top]
                    ans+= h*distance
            stack.append(i)
        return ans