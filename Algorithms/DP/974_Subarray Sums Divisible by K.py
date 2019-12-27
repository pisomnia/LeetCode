class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        
        hashmap={}
        hashmap[0]=1
        sum=0
        for num in A:
            sum+=num
            hashmap[sum%K]=hashmap.get(sum%K,0)+1
        count=0
        for value in hashmap.values():
            count+=value*(value-1)/2
        return count
        """
        dp=[0]*(len(A)+1)
        N=len(A)+1
        prefix_sum=[0]*N
        res=0
        for i in range(1,N):
            prefix_sum[i]=prefix_sum[i-1]+A[i-1]
        for i in range(1,N):
            for j in range(i-1,-1,-1):
                if ((prefix_sum[i] - prefix_sum[j]) % K == 0):
                    dp[i]=dp[j]+1
                    res+=dp[i]
                    break
        return res
        
