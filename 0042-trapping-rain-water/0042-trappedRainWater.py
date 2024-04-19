class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Bidirectional Dec. and Con. or 2 pointers approach
        # lets assume there are two towers on both of the ends, i and j, and move i and j depending on the 
        # shorter height
        localwaterlevel = 0
        globalwaterlevel = 0
        trappedwater = 0
        i = 0
        j = len(height) - 1

        # if i<j, then loop stops at i=j, then there will be an extra round of calculations which is not required
        while i < j-1: 
            # your calculation at ith or jth index, we are calcualting the trapped water anount and the global level and passing it down to the subordinate

            # get the water level at the ith OR jth index
            localwaterlevel = min(height[i], height[j]) 
            # trapped water tells us the extra amount of water that got added at every index if the water level increases
            if localwaterlevel > globalwaterlevel:
                trappedwater += (j-i-1) * (localwaterlevel - globalwaterlevel)
                globalwaterlevel = localwaterlevel
            
            # your next subordinate's calcualtion at either i+1 or j-1 th index
            # reduce the amount of the water from the trapped amount corresponding to the height of the black column 
            if height[i] <= height[j]:
                i += 1
                trappedwater -= min(height[i], globalwaterlevel)
            else:
                j -= 1
                trappedwater -= min(height[j], globalwaterlevel)

        return trappedwater         