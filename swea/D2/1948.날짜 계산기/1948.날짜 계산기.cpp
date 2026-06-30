#include <iostream>

using namespace std;

int T, M[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int main (){
    cin >> T;

    for(int t = 1; t <= T; t++){
        int m1, d1, m2, d2, days1 = 0, days2 = 0;
        cin >> m1 >> d1 >> m2 >> d2;

        for(int i = 1; i < m1; i++)
            days1 += M[i];
        
        for(int i = 1; i < m2; i++)
            days2 += M[i];

        int ans = days2 + d2 - days1 - d1 + 1;

        cout << '#' << t << ' ' << ans << endl;
    }
}