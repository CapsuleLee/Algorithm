#include <iostream>

using namespace std;

int main(){
    int n, count;

    cin >> n;
    int ary[n];

    for(int i =0; i<n;i++){
        int h;
        cin >> h;
        ary[i]=h;
    }
    count =1;
    int criteria = ary[n-1];
    for(int i =n-2; i>=0;i--){
        if (criteria < ary[i]){
            count++;
            criteria = ary[i];
        }
            
    }
    cout << count;

}