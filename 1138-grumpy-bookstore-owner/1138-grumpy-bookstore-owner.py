class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        # Fixed length sliding window
        # DC: at the nth minute, i will see if the owner is grumpy or not
        # if he is grumpy, then i will add customers to not satisfied
        windowsum = 0
        for i in range(0, minutes):
            if grumpy[i] == 1:
                windowsum += customers[i]
        globalmax = windowsum

        #note that while maximizing we are only taking into account the grumpy minutes
        n = len(customers)
        for i in range(minutes, n):
            if grumpy[i] == 1:
                windowsum += customers[i] 
            if grumpy[i - minutes] == 1:
                windowsum -= customers[i - minutes]
            globalmax = max(globalmax, windowsum) 

        # but we need max satisfied people, so run through customeres to find all the satisfied customers as our window will only have unsatisfied people 
        satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]

        return satisfied + globalmax


