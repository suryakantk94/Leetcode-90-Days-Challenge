class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Variable Length Sliding Window

        # DC: for the subarrays ending at index i of lengths from 1 to i+1, I will move the left pointer 
        # till k allows or till their are 1s in the path to maximize the number of consecutive 1's
        # reset k when encounter index with 0 value - this will happen in the while loop, when you will subtract it
        # but no need to do it reset it to 0 all at once

        # my aim is to get the maximum lenght of subarray filled wiht ones till my index

        # maintain a window of 1s with the no of zeroes = k till index i 
        windowzeroes = 0
        left = 0
        n = len(nums)
        globalmax = 0

        for i in range(0, n):
            #for the ith index
            if nums[i] == 0:
                windowzeroes += 1
            while left <= i and windowzeroes > k:
                if nums[left] == 0:
                    windowzeroes -= 1
                left += 1
            #at the boundary where the window contains less than or equal to k 0s for index i
            if windowzeroes <= k:
                globalmax = max(globalmax, i-left+1)

        if globalmax == -1: return 0
        return globalmax