#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int T;

int main(){
    cin >> T;

    for(int t = 1; t <= T; t++){
        string s;
        cin >> s;

        string rs = s;
        reverse(rs.begin(), rs.end());

        if(rs == s)
            cout << '#' << t << ' ' << 1 << endl;
        else
            cout << '#' << t << ' ' << 0 << endl;
    }
}