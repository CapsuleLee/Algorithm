
#include <deque>
#include <algorithm>

using namespace std;



int solution(int x, int y, int n) {
    int answer = 0;
    deque<int> q;
    int ary[y+1];
    fill(ary,ary+y+1,0);
    
    q.push_back(x);
    ary[x]=1;
    
    while(!q.empty()){
        int node, searchX;
        node = q.front();
        q.pop_front();
        if(node> y){
            return -1;
        }
        
        for(int i=0; i<3; i++){
            if(i==0){
                searchX= node+n;    
            } else if(i == 1){
                searchX = node*2;
            } else{
                searchX = node*3;
            }
            if(searchX<=y){
                if(ary[searchX] == 0){
                    ary[searchX] = ary[node]+1;
                    q.push_back(searchX);
                    answer++;
                }
            }
            
        }
    }
    
    return ary[y]-1;
}