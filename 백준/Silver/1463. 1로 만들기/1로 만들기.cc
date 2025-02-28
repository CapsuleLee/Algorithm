#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(){

    int n, count=1;
    queue<int> q;
    cin >> n;
    int ary[n+1];
    fill(ary,ary+n+1,0);
    ary[n]=count;
    q.push(n);
    while(!q.empty()){
        int node, search;
        node = q.front();
        q.pop();

        for(int i =1; i<=3; i++){
            if(i==1){
                search = node-1;
            } else if(i==2 && node%i ==0){
                search = node/2;
            } else if(i == 3 && node%i==0){
                search = node/3;
            }
            if(ary[search] == 0){
                ary[search]=ary[node]+1;
                count++;
                q.push(search);
            }
        }
    }
    cout << ary[1]-1;
}