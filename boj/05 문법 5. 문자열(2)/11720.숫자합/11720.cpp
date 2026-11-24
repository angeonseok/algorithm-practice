#include <iostream>
#include <string>

using namespace std;

int main(){
    int n, ans = 0;
    cin >> n;

    string s;
    cin >> s;

    for(int i = 0; i < n; i++)  ans += s[i] - '0';

    cout << ans;
}