// new python solution based on 2 pointers approach

class Solution(object) : def trap(self, height) : ""
                                                  "
    : type height : List[int]
    : rtype : int ""
                  "
#Bidirectional Dec.and Con.or 2 pointers approach
#lets assume there are two towers on both of the ends, i and j, and move i and j depending on the
#shorter height
              localwaterlevel = 0 globalwaterlevel = 0 trappedwater = 0 i = 0 j = len(height) - 1

#if i < j, then loop stops at i = j, then there will be an extra round of calculations which is not required
                                                                                      while i <
                                                                                  j - 1 :
#your calculation at ith or jth index, we are calcualting the trapped water anount and the global level and passing it down to the subordinate

#get the water level at the ith OR jth index
    localwaterlevel = min(height[i], height[j])
#trapped water tells us the extra amount of water that got added at every index if the water level increases
                          if localwaterlevel
                      > globalwaterlevel : trappedwater
              += (j - i - 1) * (localwaterlevel - globalwaterlevel)
                                   globalwaterlevel = localwaterlevel

#your next subordinate's calcualtion at either i+1 or j-1 th index
#reduce the amount of the water from the trapped amount corresponding to the height of the black column
                                                      if height[i] <= height[j] : i
              += 1 trappedwater
              -= min(height[i], globalwaterlevel) else : j
                                                         -= 1 trappedwater
                                                         -= min(height[j], globalwaterlevel)

                                                             return trappedwater

                                                         ///////////////////////////////////////////////////////////////////
                                                         class Solution
{
public:
    int trap(vector<int> &height)
    {
        // if (height.size() == 0) {
        //     return 0;
        // }

        // time complexity O(n^2) - 320/322 test cases passed - TLE error

        // int l = 0, r = 0;
        // int res = 0; // Initialized to zero

        // for (int i = 0; i < height.size(); i++) {
        //     l = (i == 0) ? height[i] : max(l, height[i]);

        //     r = height[i];
        //     for (int k = i+1; k < height.size(); k++) {
        //         r = max(r, height[k]);
        //     }

        //     res += min(l, r) - height[i];
        // }

        // return res;

        // OPTIMIZED SOLUTION - O(n)
        // pre compute the value of maximum left height and right height for every i in a separate array in O(n) each
        int n = height.size();

        vector<int> left(n);
        vector<int> right(n);

        left[0] = height[0];
        for (int i = 1; i < n; i++)
        {
            left[i] = max(height[i], left[i - 1]);
        }

        right[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--)
        {
            right[i] = max(right[i + 1], height[i]);
        }

        int res = 0;
        for (int i = 0; i < n; i++)
            res += min(left[i], right[i]) - height[i];

        return res;
    }
};
