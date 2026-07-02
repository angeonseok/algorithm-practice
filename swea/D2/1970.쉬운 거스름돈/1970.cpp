#include <iostream>

using namespace std;

int m[8] = {50000, 10000, 5000, 1000, 500, 100, 50, 10}, T;

int main(){
    cin >> T;

    for(int t = 1; t <= T; t++){
        int n, ans[8] = {0};
        cin >> n;

        for(int i = 0; i < 8; i++){
            ans[i] = n / m[i];
            n %= m[i];
        }

        cout << '#' << t << endl;
        for(int i = 0; i < 8; i++){
            cout << ans[i] << ' ';
        }
        cout << endl;
    }
}