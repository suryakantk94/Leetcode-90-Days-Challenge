class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<int> dq;  // will store indices
        
        for (int j = 0; j < nums.size(); j++) {
            // Remove indices that are out of the current window
            while (!dq.empty() && dq.front() < j - k + 1) {
                dq.pop_front();
            }
            
            // Remove smaller numbers as they are useless
            while (!dq.empty() && nums[dq.back()] < nums[j]) {
                dq.pop_back();
            }
            
            // Add current number's index
            dq.push_back(j);
            // cout<<nums[dq.back()]<<endl;
            
            // dq.front() will always have the maximum for current window
            if (j >= k - 1) {
                res.push_back(nums[dq.front()]);
            }
        }
        
        return res;
    }
};
