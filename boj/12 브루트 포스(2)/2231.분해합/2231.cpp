#include <iostream>

using namespace std;

int main(){
    int n, ans = 0;  cin >> n;

    for(int i = 1; i <= n; i++){
        int a = i, s = 0;
        while(a > 0){
            s += a % 10;
            a /= 10;
        }

        if(s + i == n){
            ans = i;
            break;
        }
    }

    //생성자 없을 때 출력 깜빡함
    cout << ans;
}