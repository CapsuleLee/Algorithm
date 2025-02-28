#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long long solution(long long n) {
    long long answer=0;
    vector<long long> ary;
    string temp;
    string result;
    temp = to_string(n);
    for(char a :temp){
        ary.push_back(a-'0');
    }
    sort(ary.begin(),ary.end(),greater<int>());
    for(int i =0; i<ary.size();i++){
        result+=to_string(ary[i]);
    }
    answer = stoll(result);
    return answer;
}