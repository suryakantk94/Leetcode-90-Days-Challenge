class Solution {
public:

void helper(vector<int> &nums, vector<int> slate, vector<vector<int>>&result, int idx){
    
    if(nums.size() == idx){
        result.push_back(slate);
        return;
    }
    
    helper(nums, slate, result, idx+1); //exclusion
    slate.push_back(nums[idx]);
    helper(nums, slate, result, idx+1); //inclusion
    
}
    vector<vector<int>> subsets(vector<int>& nums) {
        
        int idx = 0;
        vector<vector<int>> result;
        vector<int> slate;

        helper(nums, slate, result, idx);  

        return result;     
    }
};