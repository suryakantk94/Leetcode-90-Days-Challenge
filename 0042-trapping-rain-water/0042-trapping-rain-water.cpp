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
