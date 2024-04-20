class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # DC - As the ith element, i will see if i am the max from previous max AND before that, 
        # if the previous max was the i-k th element
        # I assume that i get the previous max from my subordinate - wrong assumption in the sense
        # that getting max may take O(k) TC

        # this solution ends up being O(nk) with TLE and being more like Brute Force than DC

        """
        ans = []
        currMax = max(nums[0:k])
        ans.append(currMax)

        for i in range(k, len(nums)):
            if nums[i-k] == currMax:
                # takes O(k)
                # this is causing TLE 
                currMax = max(nums[i-k+1:i+1]) # need to recalculate the max for this window

            if nums[i] > currMax:
                currMax = nums[i]

            ans.append(currMax)
        return ans
        """

        ## We need to use some other DS which can give :
        # 1. Max in O(1), 2. Insertion of ele in front in O(1), 3. Deletion from back in O(1)
        # using a maxheap will give us O(logk) TC for 2 and 3 ops.

        # we can use a queue while maintaining the max ele for this
        q = deque()
        ans = []
        for i in range(k):
           #delete the back ele if its smaller than the incoming ith ele
            while(q and nums[i] > q[-1]):
                q.pop()
            q.append(nums[i])    
        ans.append(q[0]) 

        for i in range(k, len(nums)):
            #remove the nums[i-k] and add nums[i] as we do for fixed sliding window problems
            # only remove if its at the front of q
            if nums[i-k] == q[0]: #front ele is the curr max ele
                q.popleft() 
            ## else it would have been removed already    
            #delete the back ele if its smaller than the incoming ith ele
            while(q and nums[i] > q[-1]):
                q.pop()
            q.append(nums[i])    
            ans.append(q[0])

        return ans  
