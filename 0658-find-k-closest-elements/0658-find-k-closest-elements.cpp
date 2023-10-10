class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        priority_queue<pair<int, int>>maxh; 

        for (int i=0; i<arr.size(); i++){
            
            maxh.push({abs(x - arr[i]), arr[i]});

            if(maxh.size() > k){
                maxh.pop();
            }
        }
        priority_queue<int, vector<int>, greater<int>>temp;
    vector<int> res;
    while(maxh.size() != 0){
        // res.push_back(maxh.top().second);
        temp.push(maxh.top().second);
        maxh.pop();
    }
    while(temp.size() != 0){
        res.push_back(temp.top());
        temp.pop();
    }
    return res;
    }
};