class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ## Two pointers approach or bidirectional dec. and Con.
        ## the given example is slightly misguiding in the figure as there's no width of the bars

        n= len(height)
        i = 0
        j = n-1
        maxArea = 0

        while i < j:
            maxArea = max(maxArea, ((j-i) * min(height[i], height[j])))

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1    

        return maxArea