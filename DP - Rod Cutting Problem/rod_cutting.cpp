
int get_maximum_profit(vector<int> &price) {
    // Write your code here.
    
    int N = price.size();
    
    int dp[N+1][N+1];
    
    int length[N];
    
    for(int i = 1; i <= N; i++){
        length[i-1] = i;
    }
    // for(int i=0;i<=N;i++)
    //     dp[i][0] = 0;
    
    //   for(int j=0;j<=N;j++)
    //     dp[0][j] = 0;
        
    for(int i = 0; i <=N; i++){  // traversing length array
        for(int j = 0; j<=N; j++){ //traversing price array
            if(i == 0 || j==0){
                dp[i][j] = 0;
                continue;
        }
        if (length[i-1] <= j){
            dp[i][j] = max(dp[i-1][j], price[i-1] + dp[i][j-length[i-1]]);
        }
        else{
            dp[i][j] = dp[i-1][j];
        }
        
    }
}
return dp[N][N];
}
