#include <stdio.h>
#include <iostream>
#include<string>
#include <map>

using namespace std;

int main() {

	string word;
	map<char, int> alpa;
	cin >> word;
	
	for (char i = 97; i < 97 + 26; i++) {
		alpa.insert({ i, 0 });
	}

	int check[26];
	fill(check, check + 26, -1);
	
	for (int i = 0; i< word.size();i++) {
		if(alpa[word[i]] == 0)
			alpa[word[i]] = i+1;
	}
	int temp = 0;
	for (pair<char, int> p : alpa) {
		
		check[temp] = p.second - 1;
		temp++;
	}
	for (int i = 0; i < 26; i++) {
		cout << check[i] << " ";
	}
	
}