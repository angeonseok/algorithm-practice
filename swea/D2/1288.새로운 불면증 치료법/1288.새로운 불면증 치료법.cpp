#include <iostream>

using namespace std;

int T;

int main(){
    cin >> T;

    for(int t = 1; t <= T; t++){
        int n, arr[10] = {0};
        cin >> n;

        int cnt = 0, ans = 0, k = 1;
        while(cnt != 10){
            int tmp = n * k;
            ans = tmp;

            while(tmp != 0){
                int r = tmp % 10;
                if(arr[r] == 0){
                    arr[r]++;
                    cnt++;
                }

                tmp /= 10;
            }

            k++;
        }

        cout << '#' << t << ' ' << ans << endl;
    }
}