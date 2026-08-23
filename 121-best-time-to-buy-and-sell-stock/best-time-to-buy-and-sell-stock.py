class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p=0
        b=float("inf")
        for i in range(len(prices)):
            b=min(b,prices[i])
            p=max(p,prices[i]-b)
        return p