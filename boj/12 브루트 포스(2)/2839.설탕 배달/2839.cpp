#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, cnt = 0;  cin >> n;
    
    while(n > 0){
        if(n % 5 == 0){
            cnt += (n / 5);
            n = 0;
            break;
        }

        n -= 3;
        cnt++;
    }
    
    if(n != 0)  cnt = -1;

    cout << cnt;
}