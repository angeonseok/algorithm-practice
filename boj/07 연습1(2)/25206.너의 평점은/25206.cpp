#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(){
    string a, g;
    double b, ans = 0, cnt = 0;

    for(int i = 0; i < 20; i++){
        cin >> a >> b >> g;
        
        if(g == "P")  continue;
        if(g == "A+")  ans += 4.5 * b;
        else if(g == "A0")  ans += 4.0 * b;
        else if(g == "B+")  ans += 3.5 * b;
        else if(g == "B0")  ans += 3.0 * b;
        else if(g == "C+")  ans += 2.5 * b;
        else if(g == "C0")  ans += 2.0 * b;
        else if(g == "D+")  ans += 1.5 * b;
        else if(g == "D0")  ans += 1.0 * b;

        cnt += b;
    }
    
    cout << fixed << setprecision(6) << ans / cnt;
}