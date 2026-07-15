class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        prfit=0
        for price in prices :
            buy=min(buy,price)
            prfit=max(prfit,price-buy)
        return prfit
        