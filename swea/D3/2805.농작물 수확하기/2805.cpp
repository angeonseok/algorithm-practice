#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

int T;

int main(){
  cin >> T;
  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;
    
    vector<string> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    int mid = n / 2, ans = 0;

    for(int i = 0; i < n; i++){
      int diff = abs(mid - i);

      for(int j = diff; j < n - diff; j++){
        ans += arr[i][j] - '0';
      }
    }

    cout << '#' << t << " " << ans << '\n';
  }
}