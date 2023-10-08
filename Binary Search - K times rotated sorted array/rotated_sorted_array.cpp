//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	int findKRotation(int arr[], int n) {
	    // code here
	    int start = 0;
	    int end = n-1;
	    int mid = 0;
	    int next = 0;
	    int prev = 0;
	    
	    while(start <= end){
	          mid = start + (end - start) / 2;
	    next = (mid + 1 ) % n;
	     prev = (mid + n - 1) % n;
	     
	        if(arr[mid] <= arr[next] && arr[mid] <= arr[prev] ){
	            return mid;
	        }
	        if(arr[mid] >= arr[end]){
	            start = (mid + 1 );
	        }
	        else{
	            end = (mid - 1);
	        }
	    }
	    
	    
	}

};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findKRotation(a, n);
        cout << ans << "\n";
    }
    return 0;
}

// } Driver Code Ends