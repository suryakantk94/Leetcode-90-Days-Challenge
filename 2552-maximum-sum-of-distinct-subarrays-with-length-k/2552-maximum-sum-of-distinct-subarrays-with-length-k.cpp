class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        if (k > n) return 0;

        unordered_set<int> s;
        long long sum = 0, ans = 0;
        int i = 0;

        for (int j = 0; j < n; ++j) {
            // Remove duplicates if found
            while (s.find(nums[j]) != s.end()) {
                s.erase(nums[i]);
                sum -= nums[i];
                i++;
            }

            // Insert current number into set and add to sum
            s.insert(nums[j]);
            sum += nums[j];

            // If current window size is k, update the answer
            if (j - i + 1 == k) {
                ans = max(ans, sum);
                // Move the window
                s.erase(nums[i]);
                sum -= nums[i];
                i++;
            }
        }
        return ans;
    }
};
