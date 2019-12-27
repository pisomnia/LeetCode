class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        hold=[0]*len(prices)
        unhold=[0]*len(prices)
        hold[0]=-prices[0]
        for i in range(1,len(prices)):
            hold[i]=max(hold[i-1],unhold[i-1]-prices[i])
            unhold[i]=max(hold[i-1]+prices[i]-fee,unhold[i-1])
        return unhold[-1]