class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        f = [0] * n
        g = [0] * n

        f[0] = -fee #if you buy and sell on the same day by definition of f[i]
        g[0] = 0 # but g[0] would be 0 because its always the max profit 
        # which will be 0 for negative fees

        for i in range(1, n):
            f[i] = prices[i] - prices[i-1] + max(g[i-1] - fee, f[i-1])
            g[i] = max(g[i-1], f[i]) 

        if g[n-1] < 0:
            return 0
        return g[n-1]
        