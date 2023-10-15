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
    int maxPathSum(TreeNode* root) {
        
        int res = INT_MIN;
        helper(root, res);
        return res;
    }
    int helper(TreeNode* root, int& res){
        
        //base condition
        //hypothesis
        //induction step
        
        if (root == NULL)
            return 0;

        int l = helper(root->left, res);
        int r = helper(root->right, res);

        int temp = max(max(l,r) + root->val, root->val);
        int ans = max(temp, l+r+root->val);
        res = max(res, ans);

        return temp;
    }
};