class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # since we have to do it in place, we will need more than one pointers to manipulate it
        # when cnt at ith index > 2 for same element, start copying the elements using the second pointer - but this will not cover every case
        # instead copy when cnt <= 2

        cnt = 1
        j = 1
        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            # now the comparison part is done, we can move the previous elements till i using j
            # as the next comparison will be with i+1 and i th element
            if cnt <= 2:
                nums[j] = nums[i]
                j += 1
        
        return j

