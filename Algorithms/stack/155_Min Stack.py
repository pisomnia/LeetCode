class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin==None or x<curMin:
            curMin=x
        self.q.append((x,curMin))
        

    def pop(self):
        """
        :rtype: None
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.q)==0:
            return None
        else:
            return self.q[len(self.q)-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q)==0:
            return None
        else:
            return self.q[len(self.q)-1][1]
        