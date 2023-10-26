#include <iostream>
#include <queue>
#include <algorithm>

//求二叉树的最大宽度
//队列
struct TreeNode {
    int val;
    TreeNode *left,*right;
    TreeNode() {
        val = 0;
        left = nullptr;
        right = nullptr;
    }
    TreeNode(int value, TreeNode *l, TreeNode *r) {
        val = value;
        left = l;
        right = r;
    }
};

void max_width_tree(TreeNode* root, int &res) {
    if (root == nullptr) {
        res = 0;
        return ;
    }
    std::queue<TreeNode*> sq;
    sq.push(root);
    while (!sq.empty()) {
        int len = sq.size();
        res = std::max(res, len);
        for (int i = 0; i < len; ++i) {
            TreeNode *cur = sq.front();
            sq.pop();
            if (cur->left != nullptr) {
                sq.push(cur->left);
            }
            if (cur->right != nullptr) {
                sq.push(cur->right);
            }
        }
    }
    return ;
}

int main(int argc, char const *argv[])
{
    std::vector<int> vc {1,2,3,4,5};
    int res = 0;

    return 0;
}

