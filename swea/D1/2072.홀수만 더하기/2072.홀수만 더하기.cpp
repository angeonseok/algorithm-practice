#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++){
        int num, ans = 0;
        
        for(int i = 0; i < 10; i++){
            cin >> num;
            if(num % 2 != 0)
            ans += num;
        }
        cout << '#' << t << ' ' << ans << endl;
    }
}