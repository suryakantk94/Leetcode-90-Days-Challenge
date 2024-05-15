class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Flawed - not covering every case
        # At the ith index, i will check if the start of the newinterval is <= me, if it is, then start merging
        # else append myself nd move on 
        # use a flag to indicate to other i+1 index whether its already merged
        
        # Approach - 
        # draw a number line, take different cases in consideration with only ith interval
        # DC - as the ith interval, i will. check with myself where does newinterval lies 
        # if the newinterval lies after me totally --> append the current interval as new interval can still overlap
        # if the newinterval lies before me totally --> append the new interval, and return result as others are non-overlapping
        # if the newinterval overlaps somewhere either at start or end or both --> merge them 

        result = []
        for i in range(len(intervals)):
            
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result = result + intervals[i:]
                return result
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        result.append(newInterval)
        return result


