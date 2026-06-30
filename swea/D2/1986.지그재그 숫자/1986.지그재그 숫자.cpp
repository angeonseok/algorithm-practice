#include <iostream>

using namespace std;

int T; 

int main(){
    cin >> T;

    for(int t = 1 ; t <= T; t++){
        int n, ans = 0;
        cin >> n;
    
        for(int i = 1; i <= n; i++){
            if(i % 2 != 0)
                ans += i;
            else
                ans -= i;
        }

        cout << '#' << t << ' ' << ans << endl;
    }
}