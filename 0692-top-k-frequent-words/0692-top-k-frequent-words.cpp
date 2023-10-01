class Solution {
public:

    static bool compare(pair<string, int>a, pair<string, int>b){

        if(a.second == b.second){
            return a.first < b.first;
        }
        return a.second > b.second;
    }
    vector<string> topKFrequent(vector<string>& words, int k) {
        //make a hashmap of strings 
        unordered_map<string, int> map;

        for(int i = 0; i<words.size(); i++){
            if(map.find(words[i]) != map.end()){
                map[words[i]]++;
            }
            else{
                map[words[i]] = 1;
            }
        }

        vector<pair<string, int>> vec(map.begin(), map.end());

        sort(vec.begin(), vec.end(), compare);

        vector<string> result;

        int c = 0;

        for (const auto&p : vec ){
            // cout<<p.second<< ":" << p.first;
            if(c == k){
                break;
            }

            result.push_back(p.first);

            ++c;              
        }

        // const auto&p : vec;
        // for(int i = 0; i < k; i++){
        //     result.push_back(p.second);
        // }
        return result;
    }
};