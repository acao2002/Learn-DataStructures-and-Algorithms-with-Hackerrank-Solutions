#include <stddef.h>
#include <iostream>
#include <map> 
#include <queue> 

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

/*
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

*/

    void topView(Node * root) {
        queue <pair<int, Node*>> q;
        map<int, Node*> m;
        q.push(make_pair(0, root));
        //
        while (!q.empty()){
            auto temp = q.front();
            q.pop();
            m.insert(temp);
            if (temp.second->left){
                q.push(make_pair(temp.first-1,temp.second->left));
            }
            if (temp.second->right){
                q.push(make_pair(temp.first+1,temp.second->right));
            }
        }
        for(auto i:m) cout<<i.second->data <<" ";
        

    }

}; //End of Solution