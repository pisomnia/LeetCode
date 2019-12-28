import collections
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for path in paths:
            text=path.split(" ")
            root=text[0]
            f=text[1:]
            for file in f:
                txt, content = file.split("(")
                dic[content[:-1]] += root + "/" + txt,
        return [dic[key] for key in dic if len(dic[key]) > 1]