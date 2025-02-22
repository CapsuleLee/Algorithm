#include <stdio.h>
#include <iostream>
#include<string>
#include<cmath>

using namespace std;

int main() {

	int a, b, c;
	string temp,tempB;

	cin >> a;
	cin >> b;
	cin >> c;

	temp = to_string(a);
	tempB = to_string(b);
	int result1, result2;

	result1 = (a + b) - c;
	result2 = stoi(temp + tempB) - c;
	cout << result1 << "\n" << result2;


	
}