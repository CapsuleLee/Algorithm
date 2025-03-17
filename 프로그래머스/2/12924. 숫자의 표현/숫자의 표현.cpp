#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <iostream>
using namespace std;

int solution(int n) {
    int answer = 0;
    set <int> s;
    
    for(int i = 1; i<=int(sqrt(n)); i++){
        if(n%i ==0){
            s.insert(i);
            s.insert(n/i);
        }
    }
    for(int i : s){
        if(i%2!=0){
            answer+=1;
        }
    }
    return answer;
}