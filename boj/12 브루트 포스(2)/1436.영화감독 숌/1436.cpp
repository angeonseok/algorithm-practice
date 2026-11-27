#include <iostream>
#include <string>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, i = 666, cnt = 0;  cin >> n;

    while(cnt < n){
        if(to_string(i).find("666") != string::npos)    cnt++;
        if(cnt == n)    break;
        i++;
    }

    cout << i;
}