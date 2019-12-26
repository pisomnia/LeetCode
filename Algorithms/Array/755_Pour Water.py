class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        N = len(heights)
        for v in range(V):
            pos = K
            for i in range(K + 1, N):
                if heights[i] < heights[i - 1]:
                    pos = i
                elif heights[i] > heights[i - 1]:
                    break
            for i in range(K - 1, -1, -1):
                if heights[i] < heights[i + 1]:
                    pos = i
                elif heights[i] > heights[i + 1]:
                    break
            heights[pos] += 1
        return heights