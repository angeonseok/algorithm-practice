#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    getline(cin, s);

    int i;
    cin >> i;

    cout << s[i-1];
}