#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> number = {
    "ABC",
    "DEF",
    "GHI",
    "JKL",
    "MNO",
    "PQRS",
    "TUV",
    "WXYZ"
};

int main(){
    string s;
    cin >> s;

    int ans = 0;
    for(auto x:s){
        for(int y = 0; y < 8; y++){
            if(number[y].find(x) != string::npos)   ans += y + 3;
        }
    }

    cout << ans;
}