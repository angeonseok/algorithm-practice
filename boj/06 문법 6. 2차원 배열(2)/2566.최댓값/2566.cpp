#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<vector<int>> arr(9, vector<int>(9, 0));

    int ans = 0, x = 1, y = 1;
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            cin >> arr[i][j];

            if(arr[i][j] > ans){
                ans = arr[i][j];
                x = i + 1;
                y = j + 1;
            }
        }
    }

    cout << ans << '\n';
    cout << x << ' ' << y;
}