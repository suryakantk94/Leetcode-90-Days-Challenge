//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution{
public:
    
    void helper(string &s, int idx, string slate, vector<string> &result){
        
        if(s.size() == idx){
            result.push_back(slate);
            return;
        }    
        
        
        //inclusion    


            helper(s, idx + 1, slate + " " + s[idx], result);
  
        //exclusion
        helper(s, idx + 1, slate + s[idx], result);
    }
    
    vector<string> permutation(string s){
        // Code Here
        int idx = 1;
        string slate;
        slate = slate + s[0];
        vector<string>result;
        
        
        helper(s, idx, slate, result);
        
        return result;
    }
};

//{ Driver Code Starts.

int  main(){
    int t;
    cin>>t;
    while(t--){
        string S;
        cin>>S;
        vector<string> ans;
        Solution obj;
        ans = obj.permutation(S);
        for(int i=0;i<ans.size();i++){
            cout<<"("<<ans[i]<<")";
        }
        cout << endl;
    }
}

// } Driver Code Ends