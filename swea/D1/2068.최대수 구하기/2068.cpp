#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++){
        int a, ans = 0;        
        
        for(int i = 0; i < 10; i++){
            cin >> a;
            if(a > ans)
                ans = a;
        }

        cout << '#' << t << ' ' << ans << endl;
    }
}