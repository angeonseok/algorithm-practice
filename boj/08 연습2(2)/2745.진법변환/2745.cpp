#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
    string s;
    int b;
    long ans = 0;

    cin >> s >> b;
    reverse(s.begin(), s.end());

    for(int i = 0; i < s.length(); i++){
        int a = s[i] - '0';
        if(a >= 0 && a <= 9)    ans += a * pow(b, i);
        else    ans += (s[i] - 'A' + 10) * pow(b, i);
    }

    cout << ans;
}