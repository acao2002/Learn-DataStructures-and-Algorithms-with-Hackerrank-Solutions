#include <stddef.h>
#include <iostream>
/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht; 
};

int max(int a, int b) 
{ 
    return (a > b)? a : b; 
}


int height(node*node){
    if(node == NULL){
        return -1;
    }
    return node->ht;

}
int getBalance(node *N) 
{ 
    if (N == NULL) 
        return 0; 
    return height(N->left) - height(N->right); 
} 
node* rotatel(node*y){

    node*x = y->left;
    y->left = x->right;
    x->right = y;
    y->ht = max(height(y->left),height(y->right)) + 1;
    x->ht = max(height(x->left),height(x->right)) + 1;
    return x;
    
}
node* rotater(node*x){
    node*y = x->right;
    x->right = y->left;
    y->left = x;
    x->ht = max(height(x->left),height(x->right)) + 1;
    y->ht = max(height(y->left),height(y->right)) + 1;
    return y;
   
}
node * insert(node * root,int val)
{
        if (root == NULL){
            root = new node();
            root->val = val;
            root->ht = 0;
        }
        else if(val > root->val){
                root->right = insert(root->right,val);
        
            }
        else{
                root->left = insert(root->left,val);
        }    
        root->ht = 1 + max(height(root->left), 
                        height(root->right)); 

        int balance = getBalance(root);
        if (balance > 1 && val < root->left->val) {
            return rotatel(root);
        }
        if (balance > 1 && val > root->left->val) {
            root->left = rotater(root->left);
            return rotatel(root);
        }
        if (balance <-1 &&  val > root->right->val) {
            return rotater(root);
        }
        if (balance <-1 &&  val < root->right->val){
            root->right = rotatel(root->right);
            return rotater(root);
        }
        return root;
  
}