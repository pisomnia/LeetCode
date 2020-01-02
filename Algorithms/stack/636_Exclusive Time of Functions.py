class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        prevTime = 0
        for log in logs:
            idx, type, time = log.split(':')
            if type == 'start':
                if stack:
                    res[stack[-1]] += int(time) - prevTime
                stack.append(int(idx))
                prevTime = int(time)
            else:
                res[stack[-1]] += int(time) - prevTime + 1
                stack.pop()
                prevTime = int(time) + 1
        return res
