class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
#dp[i]代表以i结尾的能被K整除的子数组的最多个数
