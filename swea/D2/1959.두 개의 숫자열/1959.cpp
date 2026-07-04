#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T; 

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int n, m;
    cin >> n >> m;
    
    vector<int> arr1(n);
    vector<int> arr2(m);

    for(int i = 0; i < n; i++) cin >> arr1[i];
    for(int i = 0; i < m; i++) cin >> arr2[i];

    if(m > n){
      swap(n, m);
      swap(arr1, arr2);
    }

    int ans = 0;
    for(int i = 0; i <= n - m; i++){
      int total = 0;
      for(int j = 0; j < m; j++){
        total += arr1[i+j] * arr2[j];
      }

      ans = max(ans, total);
    }

    cout << '#' << t << ' ' << ans << endl;
  }
}