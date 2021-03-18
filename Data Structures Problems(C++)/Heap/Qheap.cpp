//This is not my solution, this is a C++ solution to this problem of user Biprodas on Hackkerrank

#include<iostream>

using namespace std;

#define NN 100000 //Heap size

struct minHeap{
    int n; //number of nodes in heapArr
    int heapArr[NN+1]; //array is 1 based
    minHeap(){ n=0 ;}
    void min_heapify(int index);
    void insert(int k);
    int search(int k);
    void deleteKey(int k);
    int getMin();
};
void minHeap::min_heapify(int i){
        int l = 2*i;
        int r = 2*i+1;
        int min = i;
        if(l<n && heapArr[l]<heapArr[min])
            min = l;
        if(r<n && heapArr[r]<heapArr[min])
            min = r;
        if(min != i){
            swap(heapArr[i],heapArr[min]);
            min_heapify(min);
        }
    }
void minHeap::insert(int k){
        if(n==NN) return;
        n++;
        heapArr[n]= k;
        int p= n;
        while(p>1){
            int pr= p/2;
            if(heapArr[pr]>heapArr[p]){
                swap(heapArr[pr],heapArr[p]);
                p= pr;
            }
            else break;
        }
}
int minHeap::getMin(){
    if(n==0) return -1;
    else return heapArr[1];
}

int minHeap::search(int ele){
    for(int i=1;i<=n;i++){
        if(heapArr[i] == ele)
            return i;
        }
        return -1;
    }

void minHeap::deleteKey(int ele){
        int index = search(ele);
        heapArr[index] = heapArr[n];
        n--;
        min_heapify(index);
    }
int main(){
    minHeap h;
    int q, t, x;
    cin>>q;
    while(q--){
        cin>>t;
        if(t==1){
            cin>>x;
            h.insert(x);
        }
        else if(t==2){
            cin>>x;
            h.deleteKey(x);
        }
        else{
            cout<<h.getMin()<<endl;
        }
    }
}