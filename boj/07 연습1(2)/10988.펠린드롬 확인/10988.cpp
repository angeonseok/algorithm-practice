#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    string s;
    cin >> s;

    string tmp = s;
    reverse(tmp.begin(), tmp.end());

    cout << ((s == tmp) ? 1:0);
}