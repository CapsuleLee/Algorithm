#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;


int main(){
    
    int n,m;
    cin >> n >> m;

    vector<vector<int>> graph(m,vector<int>(n,0));
    vector<vector<int>> visited(m,vector<int>(n,0));
    for(int i =0; i<m;i++){
        for(int j =0; j<n; j++){
            int x;
            cin >> x;
            graph[i][j]=x;
        }
    }
    int dx[2] = {0,1};
    int dy[2] = {1,0};

    queue<pair<int,int>> q;
    q.push(make_pair(0,0));
    visited[0][0]=1;

    while (!q.empty()){
        int nodeX, nodeY;
        nodeX = q.front().first;
        nodeY = q.front().second;
        q.pop();

        for(int i=0; i<2; i++){
            int searchX, searchY;
            searchX = dx[i]+nodeX;
            searchY = dy[i]+nodeY;

            if(0<=searchX && searchX <m && 0<=searchY && searchY < n ){
                if(visited[searchX][searchY]==0 && graph[searchX][searchY]==1){
                    visited[searchX][searchY] =1;
                    q.push(make_pair(searchX, searchY));
                }
            }
        }
    }
    if (visited[m-1][n-1]==1){
        cout << "Yes";
    }else{
        cout << "No";
    }
    
}