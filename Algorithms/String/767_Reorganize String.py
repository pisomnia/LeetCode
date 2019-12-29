class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        ans="#"
        while counter:
            stop=True
            for item,times in counter.most_common():
                if item!=ans[-1]:
                    ans+=item
                    counter[item]-=1
                    if not counter[item]:
                        del counter[item]
                    stop=False
                    break
            if stop:
                break
        return ans[1:] if len(ans[1:])==len(S) else ""
        