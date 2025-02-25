#include <iostream>

using namespace std;

bool solution(int x) {
    bool answer = false;
    int temp =0;
    int num =0;
    num = x;
    while(x>0){
        temp+= x%10;
        x/=10;
    }
    if(num % temp ==0)
        answer = true;
    return answer;
}