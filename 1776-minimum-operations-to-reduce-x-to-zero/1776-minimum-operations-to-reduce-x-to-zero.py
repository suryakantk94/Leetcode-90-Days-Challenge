class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # Variable length sliding window

        # TC/ Complement of the problem: since we have to remove the elements from starting and end only till we get x sum, we can take the complement of the problem i.e.
        # instead of minimizing we can try maximizing the sum of the middle of the array to sum(nums) - x. 

        # the leftover elements from both the sides is going to be the no of operations required to reduce x to 0

        # DC: as the ith element, i will let the left pointer come to me from left until the sum of window > sum(nums) - x
        # now the windowsum may be equal or less than k, that we have to check

        globalmax = -1
        k = sum(nums) - x # O(n)
        n = len(nums)
        windowsum = 0
        left = 0

        for i in range(0, n):
            windowsum += nums[i]
            # we will stop when windowsum > k as inside the window either the sum will be less or equal
            while left <= i and windowsum > k :
                windowsum -= nums[left]
                  
                left += 1
            # if some calcualtion needs to be done at the boundary of the window from left
            if windowsum == k:
                globalmax = max(globalmax, i-left+1)  

        if globalmax == -1: return -1   
  
        return n-globalmax
        