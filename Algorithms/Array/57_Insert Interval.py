class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        results = []
        insertPos = 0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                results.append(interval)
                insertPos += 1
            elif interval[0] > newInterval[1]:
                results.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        results.insert(insertPos, newInterval)
        return results