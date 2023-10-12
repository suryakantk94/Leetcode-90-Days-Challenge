/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        //base step
        //hypothesis step
        //induction step
        int res = INT_MIN;

        lengthOfTree(root, res);

return res - 1;
    }

    int lengthOfTree(TreeNode* root, int& res){

        if( root == NULL ){
            return 0;
        }

        int l = lengthOfTree(root->left, res);
        int r = lengthOfTree(root->right, res);

        int temp = max(l,r) + 1;
        int ans = max(temp, l+r+1);
         res = max(ans, res);

         return temp;
    }
        
};