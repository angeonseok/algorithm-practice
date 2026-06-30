#include <iostream>
using namespace std;

int T;

int main(){
    cin >> T;

    for(int t = 1; t <= T; t++){
        int n;
        cin >> n;

        int arr[10][10] = {0};

        for(int i = 0; i < n; i++){
            arr[i][0] = 1;
        }

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= i; j++){
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1];
            }
        }

        cout << '#' << t << endl;
        for(int i = 0; i < n; i++){
            for(int j = 0; j <= i; j++){
                cout << arr[i][j] << ' ';
            }
            cout << endl;
        }
    }

    return 0;
}