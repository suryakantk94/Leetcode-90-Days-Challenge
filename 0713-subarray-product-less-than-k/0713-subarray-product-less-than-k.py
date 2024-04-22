class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Variable length Slidign window

        # As the ith index where the subarray is ending at i, I will see if I make the multiplication higher than k or not, 
        # if i make it higher, then i increment the left pointer 
        # now inside thsi window every element nd their multiplication is less than k 
        count = 0
        windowproduct = 1
        left = 0
        n = len(nums)

        for i in range(0, n):
            windowproduct *= nums[i]

            # for the ith index    
            while left <= i and windowproduct >= k:
                windowproduct /= nums[left]
                left += 1

            count += (i-left + 1) 
        return count