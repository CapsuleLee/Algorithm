#include <string>
#include <vector>
#include <math.h>
#include <set>
using namespace std;

int solution(int n) {
    int answer = 0;
    set <int> s;
    
    
    for(int i =1; i<int(sqrt(n))+1; i++){
        if(n%i ==0){
            s.insert(i);
            s.insert(n/i);
            
        }
    }
    for(auto i = s.begin(); i!=s.end() ;i++){
        answer+= *i;
    }
    
    return answer;
}