class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1st approach, Prefix sum - since the numbers are from 0 to n, we can take the sum of all the numbers which is n(n+1)/2
        # take the prefix sum till the last index, subtract it from the total sum, and we will get the missing no
        
        # 2nd approach, Cycle sort - ideally there should be n+1 numbers in the array including 0, but the length of the 
        # nums is only n, so theres always a number missing 

        # apply cycle sort for special cases, when the index for a number cannot be find, break the loop eventually it will be misplaced
        n = len(nums)

        for i in range(0, n):
            while nums[i] != i:
                dest = nums[i] # dest is the number's correct index
                if nums[i] == n: #if the index for the number doesnt exist in the array
                    break
                # swap nums[i] with nums[nums[i]] i.e. dest
                nums[i], nums[dest] = nums[dest], nums[i]

        # lookout for the misplaced number or the index which do not contain the same number
        for i in range(0, n):
            if nums[i] != i:
                return i
        
        return n #if the missing number is the n itself - EXAMPLE 2 case
