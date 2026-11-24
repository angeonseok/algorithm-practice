#include <iostream>
#include <string>

using namespace std;

int main(){
    int n;
    cin >> n;

    for(int tc = 0; tc < n; tc++){
        string s;
        cin >> s;

        cout << s.front() << s.back() << '\n';
    }
}