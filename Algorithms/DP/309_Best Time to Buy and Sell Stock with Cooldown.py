class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold=[0]*len(prices)
        unhold=[0]*len(prices)
        if len(prices)<=1:
            return 0
        hold[0]=-prices[0]
        for i in range(1,len(prices)):
            if i==1:
                hold[i]=max(-prices[0],-prices[1])
            else:
                hold[i]=max(hold[i-1],unhold[i-2]-prices[i])
            unhold[i]=max(unhold[i-1],hold[i-1]+prices[i])
        return unhold[-1]