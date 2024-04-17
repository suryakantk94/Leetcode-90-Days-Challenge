class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Decrease and Conquer approach
        # On day i (g2(i)), there will be either no transaction at all (g2(i-1)) or there can be a transaction (f2[i])with 
        #buy date on previous day (p[i] - p[i-1] + g1[i-1])or buy date on some earlier day (p[i] - p[i-1] + f2[i-1])
        # Make a tree of decisions to be made on day i for the 2 transactions
        # there will be 2 nested trees 


        # g2[i] = Max profit that can be made with 2 transactions upto day/index i
        # g1[i] = Max profit that can be made till day i with 1 transaction
        # f2[i] = Max profit that can be made on day i with 2 transactions
        # f1[i] = Max profit that can be made on day i with 1 transaction

        n = len(prices)

        # Base Cases 
        # 0 for all arrays for index 0 acc to our def
        g2 = [0] * n 
        g1 = [0] * n
        f2 = [0] * n
        f1 = [0] * n

        for i in range(1, n):
            f1[i] = prices[i] - prices[i-1] + max(0, f1[i-1])
            g1[i] = max(g1[i-1], f1[i])
            f2[i] = prices[i] - prices[i-1] + max(g1[i-1], f2[i-1])
            g2[i] = max(g2[i-1], f2[i])

        return g2[-1]
        