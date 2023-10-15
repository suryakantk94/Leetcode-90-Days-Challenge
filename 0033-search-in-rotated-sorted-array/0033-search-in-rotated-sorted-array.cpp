class Solution {
public:
    int getMinIndex(vector<int> nums){
        int n = nums.size();
        int start = 0, end = n-1;


        while(start <= end){
        int mid = start + (end - start) / 2;
        int next = (mid + 1) % n;
        int prev = (mid + n - 1) % n;

        if(nums[mid] <= nums[prev] && nums[mid] <= nums[next]){
            return mid;
        }

        if (nums[mid] >= nums[end]){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }


        }
        return -1;
    }
    int getTarget(vector<int> nums, int start, int end, int target){
        int n = nums.size();
        // int start = 0, end = n-1;


        while(start <= end){
        int mid = start + (end - start) / 2;
        int next = (mid + 1) % n;
        int prev = (mid + n - 1) % n;

        if(nums[mid] == target){
            return mid;
        }

        if (nums[mid] <= target){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }


        }
        return -1;
    }
    int search(vector<int>& nums, int target) {
        int K = getMinIndex(nums);
        cout<<K<<endl;
                int n = nums.size();

        if(nums[K] == target){
            return K;
        }

        int L = getTarget(nums, 0, K-1, target);
        int R = getTarget(nums, K+1, n-1, target);

        if (L == -1 && R == -1)
            return -1;
        if(L != -1)
            return L;
        else
            return R;
        //
        return 0;
    }
};