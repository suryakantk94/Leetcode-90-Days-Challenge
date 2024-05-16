
def bs(nums, target):

    start = 0
    end = len(nums) - 1

    while (start <= end):
        mid = start + (end-start) // 2
        # print(mid)
        if ( target == nums[mid] ):
            return mid
            
        if ( target > nums[mid]):
            start = mid + 1
        else:    
            end = mid - 1
    return start


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sorted array - use binary search instead of linear search, O(n)
        # that will make the TC log n

        return bs(nums, target)

        