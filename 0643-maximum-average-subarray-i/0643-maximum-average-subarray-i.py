class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Fixed length Sliding window problem

        # DC: for the last element, you will have the sum of the window till n-1th element.
        # now you add yourself, and subtract the k th element

        # first take the sum of the first k elements without which the avg cant be calculated
        windowsum = sum(nums[0:k]) #sum from 0 to k-1 index of elements
        # since we have to return max 
        maxwindowsum = windowsum

        #first k elements are already covered
        for i in range(k, len(nums)): #from k to n-1
            windowsum += (nums[i] - nums[i-k])
            maxwindowsum = max(maxwindowsum, windowsum) 

        return float(maxwindowsum)/k    #taking float of both results in wrongly formatted answer


