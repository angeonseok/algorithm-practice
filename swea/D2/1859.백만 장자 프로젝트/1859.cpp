#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i = 0; i < n; i++) cin >>arr[i];

    reverse(arr.begin(), arr.end());
    
    int max_p = 0;
    long long ans = 0;
    for(int x : arr){
      if(x > max_p) max_p = x;
      else ans += max_p - x;
    }

    cout << '#' << t << ' ' << ans << endl;
  }
}