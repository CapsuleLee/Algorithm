#include <cmath>
using namespace std;
long long solution(long long n) {
    long long temp ;
    temp= int(sqrt(n));
    if (n / temp == temp && n % temp == 0)
        return (temp+1)*(temp+1);
    return -1;
}