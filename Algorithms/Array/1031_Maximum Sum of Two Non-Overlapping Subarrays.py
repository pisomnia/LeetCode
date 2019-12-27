class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        if L+M>len(A):
            return
        prefix_sum=[0]*len(A)
        prefix_sum[0]=A[0]
        for i in range(1,len(A)):
            prefix_sum[i]=prefix_sum[i-1]+A[i]
            
        maxSum1=self.getMax(prefix_sum,A,L,M)
        maxSum2=self.getMax(prefix_sum,A,M,L)
        return max(maxSum1,maxSum2)
    
    def getMax(self,pre_sum,A,L,M):
        maxL=0
        maxSum=0
        for i in range(L+M-1,len(A)):
            if i-M-L>=0:
                maxL=max(maxL,pre_sum[i-M]-pre_sum[i-M-L])
            else:
                maxL=max(maxL,pre_sum[i-M])
            maxSum=max(maxSum,maxL+pre_sum[i]-pre_sum[i-M])
        return maxSum