class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """       
        
        new_t = []
        for time in timePoints:
            temp_t = time.split(":")
            new_t.append(int(temp_t[0]) * 60 + int(temp_t[1]))
        new_t = sorted(new_t)
        min_t = 10000000
        for i in range(len(new_t)-1):
            if(abs(new_t[i] - new_t[i+1]) < min_t):
                min_t = abs(new_t[i] - new_t[i+1])
        if(len(new_t) > 1 and (24*60 - new_t[-1] + new_t[0]) < min_t):
            min_t = 24*60 - new_t[-1] + new_t[0]
        return min_t