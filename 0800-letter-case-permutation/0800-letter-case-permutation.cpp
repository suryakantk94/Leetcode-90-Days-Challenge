class Solution {
public:
    
    

    vector<string> letterCasePermutation(string s) {
        
        int idx = 0;
        vector<string> res;
        string slate;

        helper(s, idx, slate, res);

        return res;
    }
    void helper(string &s, int idx, string slate, vector<string> &res){

        if(s.size() == idx){
            res.push_back(slate);
            return;
        }

        // if(isdigit(s[idx]))
        if(s[idx] >= '0' && s[idx] <= '9'){
            helper(s, idx+1, slate + s[idx], res);
        }
        else{
        char low = tolower(s[idx]);
        helper(s, idx+1, slate + low, res);

        char up = toupper(s[idx]);
        helper(s, idx+1, slate + up, res);
        }

    }
};