#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;

    int ans = a - b;

    if(ans < 0)
        ans *= -1;

    cout << ans + 1;
}