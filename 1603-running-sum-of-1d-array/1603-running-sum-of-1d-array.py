class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # PREFIX SUMS type
        # keep running sum stored at every index in the array
        prefixsum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            prefixsum.append(sum)
        
        return prefixsum
