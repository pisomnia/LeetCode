# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        if n<1:
            return -1
        if n<2:
            return n
        for i in range(1,n):
            if knows(ans,i):
                ans=i
        for j in range(n):
            if j!=ans and knows(ans,j):
                return -1
            if j!=ans and not knows(j,ans):
                return -1
        return ans