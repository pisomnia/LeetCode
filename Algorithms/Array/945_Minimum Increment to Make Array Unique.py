class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        if N == 0: return 0
        A.sort()
        res = 0
        prev = A[0]
        for i in range(1, N):
            if A[i] <= prev:
                prev += 1
                res += prev - A[i]
            else:
                prev = A[i]
        return res