#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int a, b, v;
    cin >> a >> b >> v;

    int ans = 1 + (v - a) / (a - b);
    if((v - a) % (a - b))   ans++;
    
    cout << ans;
}