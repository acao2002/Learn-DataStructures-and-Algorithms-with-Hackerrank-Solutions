#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
using namespace std;

int max(int a, int b){
    return a>b?a:b;
}
int main() {
    
    list<int> maxq;
    int n; 
    cin >> n; 
    for(int i = 0; i<n; i++){
        int inp, item;
        cin >> inp;
        if (inp == 1){
            cin >> item;
            if (maxq.empty()){
                maxq.push_back(item);
            }
            else {
                maxq.push_back(max(item,maxq.back()));
            }
        }
        if(inp == 2){
            maxq.pop_back();
        }
        if(inp == 3){
            cout << maxq.back() << endl;
        }
    }
    return 0;
}
