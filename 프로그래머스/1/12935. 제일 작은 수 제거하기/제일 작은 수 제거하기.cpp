
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    
    int idx = min_element(arr.begin(),arr.end())-arr.begin();
    arr.erase(arr.begin()+idx);
    if(arr.empty()){
        arr.push_back(-1);
    }
    return arr;
}