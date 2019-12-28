class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ans=''
        num=0
        for c in "!?',;.":
            paragraph=paragraph.replace(c," ")
        count = collections.Counter(paragraph.lower().split())
        for word in count:
            if count[word]>num and word not in banned:
                ans=word
                num=count[word]
        return ans