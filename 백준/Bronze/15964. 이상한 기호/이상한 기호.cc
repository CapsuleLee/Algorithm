#include <stdio.h>
#include <iostream>


using namespace std;

int fun(int a, int b) {
	return (a + b) * (a - b);
}

int main() {

	int a, b;
	cin >> a >> b;
	cout<<fun(a, b);
}