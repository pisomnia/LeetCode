class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """             
        if not s or len(s)==0:
            return 0
        unique_set=set([])
        length=0
        j=0
        n=len(s)
        for i in range(n):
            while j <n and s[j] not in unique_set:
                unique_set.add(s[j])
                j+=1
            length=max(length,j-i)
            unique_set.remove(s[i])
        return length