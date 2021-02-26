#include <stddef.h>
#include <iostream>

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }
/*The tree node has data, left child and right child 
class Node {
    int data;
    Node* left;
    Node* right;
};

*/
    int height(Node* root) {
        int lefth = 0; 
        int righth = 0; 
        if (root->left != NULL){ 
            lefth = 1 + height(root->left);
        }
        if(root->right != NULL ) {
            righth = 1 + height(root->right);
        }
        
        return (lefth > righth) ? lefth:righth;
    }

}; //End of Solution