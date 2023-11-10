class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        
        // if(target == 'z')
        //     return letters[0];

        int n = letters.size();
        int start = 0;
        int end = n-1;
        char ans = '#';

        while(start <= end){

            int mid = start + (end - start)/2;

            if(letters[mid] == target){
                start = mid + 1;
            }
            // else 
            // if(letters[mid] >= target ){
            //     ans = letters[mid];
            // }

            if(target < letters[mid]){
                ans = letters[mid];
                end = mid - 1;
            }
            else{
                start = mid + 1;
            }
        }

        if (ans == '#')
            return letters[0];
        return ans;
    }

    
};