class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n=len(chars)
        cur=0
        i=0
        while i<n:
            j=i
            while j<n-1 and chars[j+1]==chars[j]:
                j+=1
            chars[cur]=chars[i]
            cur+=1
            if (j!=i):
                for k in range(len(str(j-i+1))):
                    chars[cur+k]=str(j-i+1)[k]
                cur+=len(str(j-i+1))
            i=j+1
        return cur