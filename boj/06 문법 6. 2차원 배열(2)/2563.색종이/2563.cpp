#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;

    vector<vector<int>> arr(100, vector<int>(100, 0));
    for(int i= 0; i < n; i++){
        int a, b;
        cin >> a >> b;

        for(int j = a - 1; j < a + 9; j++){
            for(int k = b - 1; k < b + 9; k++){
                arr[j][k] ++;
            }
        }
    }

    int ans = 0;
    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            if(arr[i][j] != 0)  ans++;
        }
    }

    cout << ans;
}