#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++){
        int a, total = 0;

        for(int i = 0; i < 10; i++){
            cin >> a;
            total += a;
        }

        cout << '#' << t << ' ' << round(total /10.0) << endl;
    }
}