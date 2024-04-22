class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        #Variable Length Sliding Window

        # DC As the ith index, i will contribute myself to the target sum, if adding me makes the target, i will take the count 
        # and update the global min count or the length of my subarray with target
        # I expect from my subordinates that i get the target 

        n = len(nums)
        # Start with Maximum lenght of subarray + 1 as global maximum 
        globalmin =  n+1
        windowsum = 0

        left = 0
        for i in range(0, n):
            windowsum += nums[i]      # get the total sum till the ith element
            while left <= i and windowsum >= target:    
                windowsum -= nums[left]  # start shrinking the window from left if we reach the target sum for an index i
                #since we are removing elements from windowsum, we will actually reach the target sum one element before going to the next element 
                globalmin = min(globalmin, i-left+1) # lenght of the subarray
                left += 1 

        if globalmin == n+1: return 0
        return globalmin



        