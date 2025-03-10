#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    vector<string> ::iterator it;
    it=find(seoul.begin(), seoul.end(),"Kim");
    string temp= to_string(it - seoul.begin());
    answer = "김서방은 "+temp+"에 있다";
    return answer;
}