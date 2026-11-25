#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n;
    cin >> n;

    int ans = pow(2, n) + 1;

    cout << ans * ans;
}