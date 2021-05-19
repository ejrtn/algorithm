class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 2:
            if prices[1]-prices[0]>0:
                return prices[1]-prices[0]
        
        a = prices[0]
        m=0
        for x in range(1,len(prices)):
            if prices[x] - a > m:
                m = prices[x] - a
            if a > prices[x]:
                a = prices[x]
            
        return m