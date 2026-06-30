#include <iostream>

using namespace std;

int T;

int main() {
    cin >> T;

    for(int t = 1; t <= T; t++){
        int h1, m1, h2, m2;
        cin >> h1 >> m1 >> h2 >> m2;

        int H = h1 + h2, M = m1 + m2;
        if(M >= 60){
            H ++;
            M -= 60;
        }

        if(H > 12){
            H -= 12;
        }

        cout << '#' << t << ' ' << H << ' ' << M << endl;
    }
}