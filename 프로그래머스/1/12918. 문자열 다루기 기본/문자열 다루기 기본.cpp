#include <string>
#include <cctype>

using namespace std;

bool solution(string s) {
    bool answer = true;
    if(s.size()==4 || s.size()==6 ){
        for(char a : s){
        
            if(isdigit(a)){
                answer = true;
            } else{
                answer = false;
                return false;
            }
        }
    } else{
            return false;
        }
    
    return answer;
}
       
    
