#include <iostream>
#include <string>
using namespace std;
    
int main(){


    long long a,b,count;
    count =0;
    string temp;
    cin >> a >> b;
    
    while(1){
        if (a == b){
            
            cout << count+1;
            break;
        } else if(a>b){
            cout << -1;
            break;
        }
        // 짝수일 때
        if (b%2 ==0){
            b/=2;
        } else{
            temp = to_string(b);
            if (temp.back() == '1'){
                temp.pop_back();
                b=stoi(temp);
            } else{
                cout << -1;
                break;
            }    
           
        }
        count++;
        
    }
}