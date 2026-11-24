#include <iostream>
#include <string>

using namespace std;

int main(){
    int n;
    cin >> n;

    for(int tc = 0; tc < n; tc++){
        int r;
        string s;
        cin >> r >> s;

        for(int i = 0; i < s.size(); i++){
            for(int j = 0; j < r; j++)  cout << s[i];
        }
        cout << '\n';
    }
}