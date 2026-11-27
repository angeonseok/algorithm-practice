#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;

    vector<int> arr(n, 0);
    for(int i = 0; i < n; i++)  cin >> arr[i];

    int ans = -1;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            for(int k = j + 1; k < n; k++){
                int s = arr[i] + arr[j] + arr[k];

                if(ans < s && s <= m)   ans = s; 
            }
        }
    }

    cout << ans;
}