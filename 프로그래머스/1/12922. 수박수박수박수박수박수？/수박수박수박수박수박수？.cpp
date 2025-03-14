#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    string ary[2] = {"수","박"};
    int idx =0;
    for(int i =0; i<n; i++){
        
        answer+=ary[idx];
        idx++;
        if(idx>1)
            idx=0;
    }
    return answer;
}