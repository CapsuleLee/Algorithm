#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;


int solution(vector<vector<int> > maps)
{
    vector<vector<int>>visited (maps.size(),vector<int>(maps[0].size(),0));
    queue<pair<int,int>> q;
    int count =1;
    int dx[4]={1,-1,0,0};
    int dy[4]= {0,0,1,-1};
    int searchX =0, searchY=0;
    int nodeX=0, nodeY=0;

    
    q.push(make_pair(0,0));
    visited[0][0] =count;
    while(not q.empty()){
        nodeX = q.front().first;
        nodeY = q.front().second;
        q.pop();
        for (int i=0; i<4;i++){
            searchX = nodeX +dx[i];
            searchY = nodeY +dy[i];

            if (0 <= searchX && searchX < maps.size() && 0 <= searchY && searchY < maps[0].size()){
                if(visited[searchX][searchY] ==0 && maps[searchX][searchY] == 1){
                    q.push(make_pair(searchX,searchY));
                    visited[searchX][searchY]= visited[nodeX][nodeY]+1;
                }
            }
        }

    }
    if (visited[maps.size()-1][maps[0].size()-1] ==0)
        return -1;
    else
        return visited[maps.size()-1][maps[0].size()-1];
    
}
