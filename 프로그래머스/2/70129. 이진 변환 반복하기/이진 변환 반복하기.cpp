#include <string>
#include <vector>
#include <bitset>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    int count,zeroCount;
    
    while (1){
        string temp;
        if(temp.size()==1)
            break;
        for(char a: s){
            if(a=='0'){
                zeroCount++;
            } else{
                temp+=a;
            }
        }
        int len = temp.size();
        temp = bitset<64>(len).to_string();
        count+=1;
    }
    answer.push_back(count,zeroCount);
    return answer;
}