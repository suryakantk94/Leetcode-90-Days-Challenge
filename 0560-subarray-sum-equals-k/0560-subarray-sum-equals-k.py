class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [1,2,3] or [1, 3, 6] k=3
        # precompute the prefixsums first for every index. 

        # approach DC - in the prefixsums, check as the ith index if subtracting k from you equals to some other prefixsums
        # index, if it does then there is a contiguous array from that index to i, if after subtracting its 0, then only that 
        # single element equals k but how will we get 

        # complement of problem - instead of total number of subarrays whose sum equals to k, 
        # search for total number of subarrays whose sum equals to prefixsums-k

        # take the complement of the approach - check at ith index in prefixsums that prefixsum(i)-k, already exists in hashmap with 
        # the count of number of subarrays leading up to this new sum, if it then increment by 1 otherwise make an entry in hashmap with 1 value

        # our hashmap contains - prefixsum(i)-k : no of subarrays that sum to this

        hmap = {}
        prefixsums = 0
        globalcount = 0

        # Base case
        hmap[0] = 1 # for prefixsum as 0, there is only one subarray that is an empty array that sums to 0
       
        for i in range(0, len(nums)):
            # for ith index
            prefixsums += nums[i]
            if prefixsums - k in hmap:
                globalcount += hmap[prefixsums - k] 

            # Update the hmap
            if prefixsums in hmap:
                hmap[prefixsums] += 1
            else:
                hmap[prefixsums] = 1

        return globalcount
