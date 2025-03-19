#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

vector<int> solution(vector <int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque <int> temp(progresses.begin(), progresses.end());
    deque <int> tempSpeeds(speeds.begin(), speeds.end());
    
    while(!temp.empty()){
        int count=0;
        int idx=temp.size();
        for(int i =0; i< idx; i++){
            temp[i]+=tempSpeeds[i];
        }
        
        for(int j=0; j<idx; j++){
            if (temp.front()>=100){
                count++;
                temp.pop_front();
                tempSpeeds.pop_front();
            } else{
                continue;
            }
        }
        if(count >0)
            answer.push_back(count);
    }
    
    return answer;
}