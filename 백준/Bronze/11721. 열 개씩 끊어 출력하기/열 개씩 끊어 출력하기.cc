#include <iostream>
#include <string>
using namespace std;

int main(){
    
    string word;
    int count=0;
    cin >> word;

    

    for(char a: word){
        cout << a;
        count++;
        if (count==10){
            count=0;
            cout << "\n";
        }
    }
}