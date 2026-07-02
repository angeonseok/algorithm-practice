#include <iostream>
using namespace std;

int T;

int main(){
    cin >> T;

    for(int t = 1; t <= T; t++){
        int a, b, n;
        cin >> a >> b >> n;

        int cnt = 0;
        while(a <= n && b <= n){
            if(a > b){
                b += a;
                cnt ++;
            }
            else{
                a += b;
                cnt ++;
            }
        }

        cout << cnt << endl;
    }
    return 0;
}