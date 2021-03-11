#include <vector>
#include <stddef.h>
#include<iostream>
#include<algorithm>
#include <numeric>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'equalStacks' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY h1
 *  2. INTEGER_ARRAY h2
 *  3. INTEGER_ARRAY h3
 */

int equalStacks(vector<int> h1, vector<int> h2, vector<int> h3) {
    int s1 = accumulate(h1.begin(), h1.end(), 0); 
    int s2 = accumulate(h2.begin(), h2.end(), 0); 
    int s3 = accumulate(h3.begin(), h3.end(), 0); 
    reverse(h1.begin(), h1.end()); 
    reverse(h2.begin(), h2.end()); 
    reverse(h3.begin(), h3.end()); 
  
    while (!h1.empty() && !h2.empty() && !h3.empty()){
        int m = min(min(s1,s2),s3);
        while (s1>m){
            s1 = s1 - h1.back();
            h1.pop_back();
        }
        while (s2>m){
            s2 = s2 - h2.back();
            h2.pop_back();
        }
        while (s3>m){
            s3 = s3 - h3.back();
            h3.pop_back();
        }
        if (s1 == s2 && s2 == s3){return s1;} 
    }
    return 0;
}
