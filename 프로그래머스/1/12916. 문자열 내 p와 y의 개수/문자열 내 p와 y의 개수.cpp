#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;

    for(int i=0; i<s.size(); i++){
        s[i] = toupper(s[i]);
    }
    int findP=0, findY=0;
    for(char alpa : s){

        if (alpa=='P'){
            findP ++;
        } else if (alpa =='Y')
        {
            findY++;
        }
    }
    if (findP == findY){
        answer = true;
    } else{
        answer = false;
    }
    

    return answer;
}