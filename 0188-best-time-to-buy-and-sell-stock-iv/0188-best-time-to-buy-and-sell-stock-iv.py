class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # for 2 transactions we needed 4 arrays in the III question - g2,g1,f2,f1
        # 2 arrays for g and 2 arrays for f
        # now for k transactions we need 2k +2 arrays (2 arrays for base cases) 
        # k arrays for g and k arrays for f 

        # gk[i] - Max profit that can be made upto day i with k transactions
        # fk[i] - Max profit that can be made on day i with k transactions
        # g(k-1)[i] - Max profit that can be made upto day i with k-1 transactions
        # f(k-1)[i] - Max profit that can be made on day i with k-1 transactions 

        # do not combine the 2k arrays into one matrix.. duhh.. coz thats not possible to calculate 
        # first row and col will be 0 as base cases for both arrays f and g
        n = len(prices)
        f = [[0] * n for r in range(k+1)] # k rows, n cols 
        g = [[0] * n for r in range(k+1)] # k rows

        for i in range(1, n): # i for number for days
            for t in range(1, k+1): # t for transactions
             
               f[t][i] = prices[i] - prices[i-1] + max(g[t-1][i-1], f[t][i-1])
               g[t][i] = max(g[t][i-1], f[t][i] ) 

        print(f)
        return g[-1][-1]




        