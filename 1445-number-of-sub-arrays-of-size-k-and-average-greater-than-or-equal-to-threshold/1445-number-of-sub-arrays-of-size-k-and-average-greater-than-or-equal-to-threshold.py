class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        # At i th index, i will add myself to the window and remove the starting element 
        # Basically fixed length sliding window

        windowsum = sum(arr[0:k])
        count = 0
        # avg = windowsum / k
        totalthreshold = threshold * k
        
        if windowsum >= totalthreshold:
            count = 1
        else:
            count = 0

        for i in range(k, len(arr)): 
            windowsum += arr[i] - arr[i-k]
            # avg = windowsum / k
            # instead of calculating avg by dividing by k, we can multiply k to get the total sum 
            if windowsum >= totalthreshold:
                count += 1

        return count 




        