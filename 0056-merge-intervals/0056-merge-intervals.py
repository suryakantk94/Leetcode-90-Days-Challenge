class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # DC - As the ith index, if my first element is <= second ele of i-1 index, then merge them
        # use stack so that if another interval with same start, so we can merge them again

        # sort the array first based off the first element as key
        intervals.sort(key = lambda x: x[0])

        # stack with first element as starting point, also handles base case
        result = [intervals[0]]

        # loop from 1st ele till end
        for start, end in intervals[1:]:
            # merging
            if start <= result[-1][1]: 
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result