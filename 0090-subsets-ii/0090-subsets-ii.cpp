class Solution {
public:
    

    void helper(vector<int> slate, vector<int>& nums, int idx, vector<vector<int>> &res){
    
    //base case
    if(nums.size() == idx ){
        // cout<<"S"<<nums.size()<<endl;
        res.push_back(slate);
        return;        
    }
    
    //store answer
        slate.push_back(nums[idx]);
    //inclusion
        helper(slate, nums, idx+1, res);
        slate.pop_back();
    
    while(idx + 1 < nums.size() && nums[idx] == nums[idx+1]){
        idx++;
    }
    // //exclusion
        helper(slate, nums, idx+1, res);
}
vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        
    // }
// vector<string> get_distinct_subsets(string &s) {
    // Write your code here.
    int idx = 0;
    vector<int> slate;
    vector<vector<int>>res;
    
    sort(nums.begin(), nums.end());
    
    helper(slate, nums, idx, res);
    
//Backtracking problem
    return res;
}

};