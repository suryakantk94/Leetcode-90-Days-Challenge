class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        //simple hashmap solution 
        // O(n) time complexity
        // O(n) space complexity
        // Space-Time TradeOff

        // unordered_map<int, int>map;
        
        // for(int i = 0; i < nums.size(); i++){
        //     if(map.find( target - nums[i] ) != map.end())
        //         return {map[ target - nums[i] ], i};
        //     map[nums[i]] = i;
        // }
        // return {};

        //method 2 - presort + two pointers - O(nlogn) + O(n) = O(nlogn) TC
        //Space complexity - O(1)


        vector<pair<int, int>> numsi;
        
        for(int i = 0; i < nums.size(); i++){
            numsi.push_back({ nums[i], i });
        }
        sort(numsi.begin(), numsi.end());

        int start = 0, end = nums.size() - 1;

        while(start < end){
            if(numsi[start].first + numsi[end].first == target)
                return {numsi[start].second, numsi[end].second};
            else if(numsi[start].first + numsi[end].first > target)
                end--;
            else
                start++;

        }

        return{};

        

    }
};