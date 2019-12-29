class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1 or numRows>=len(s):
            return s
        arr =['']*numRows
        for i in range(len(s)):
            tmp=i%(2*(numRows-1))
            if tmp<numRows:
                arr[tmp]+=s[i]
            else:
                arr[2*(numRows-1)-tmp]+=s[i]
        return ''.join(arr)
