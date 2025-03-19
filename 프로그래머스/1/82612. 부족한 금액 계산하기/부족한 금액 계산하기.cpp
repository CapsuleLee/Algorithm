#include <cmath>
using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;
    long long temp=0;
    for(int i=1; i<count+1; i++){
        temp +=price*i;  
    }
    if (money>=temp)
        return 0;
    answer = abs(temp-money);

    return answer;
}