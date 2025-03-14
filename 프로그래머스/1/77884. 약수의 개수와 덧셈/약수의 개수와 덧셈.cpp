#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int left, int right) {
    int answer = 0;

    for(int i = left; i <= right; i++){
        vector<int> ary;
        for(int j =1; j<=int(sqrt(i)); j++){
            if(i%j ==0){
                if(j == i/j){
                    ary.push_back(j);
                }else{
                    ary.push_back(j);
                    ary.push_back(i/j);
                }
            }
        }
        if(ary.size()%2 == 0){
            answer+=i;
        } else{
            answer -= i;
        }
        
    }
    return answer;
}