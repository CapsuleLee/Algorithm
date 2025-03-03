#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
using namespace std;

int solution(vector<int> arr) {
    int answer = 0;
    int temp =0;
    temp = arr[0];
    for(int i =0; i < arr.size(); i++){
        temp=lcm(temp,arr[i]);
    }
    answer = temp;
    return answer;
}