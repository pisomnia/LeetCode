from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic=defaultdict(list)
        for s in strs:
            sorted_s=''.join(sorted(s))
            dic[sorted_s].append(s)
        res=[]
        for i in dic:
            res.append(dic[i])
        return res