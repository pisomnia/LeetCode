class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
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
