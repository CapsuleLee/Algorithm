#include <stdio.h>
#include <iostream>


using namespace std;

long long fun(long long a, long long b) {
	return (a + b) * (a - b);
}

int main() {

	long long a, b;
	cin >> a >> b;
	cout<<fun(a, b);
}