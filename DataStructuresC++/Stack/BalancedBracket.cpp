#include <iostream>
using namespace std;
#include <stack>
#include <stddef.h>

// Complete the isBalanced function below.
string isBalanced(string s) {
    bool test = true;
    stack <char>q;
    int a = s.length();
    for (int i = 0; i < a; i ++){
        if ((s[i] == '(') ||(s[i] == '{')  || (s[i] == '['))       {
            q.push(s[i]);  
        }
               
        else if (!q.empty()) {
            if ((s[i] == ')' && q.top() == '(') || (s[i] == ']' && q.top() == '[') || (s[i] == '}' && q.top() == '{')) {
                q.pop();
            }
            else{
                test = false;
            }
                
        }

        else {
            test = false;
        }
             
    }       
    if (q.empty() && test){
        return "YES";
    }
        
    else{
        return "NO";
    }
      

}
