#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n, k, ans = 0;
  cin >> n;

  vector<int> arr(n);
  for(int i = 0; i < n; i++)  cin >> arr[i];

  cin >> k;
  for(int j = 0; j < n; j++){
    if(arr[j] == k) ans++;
  }

  cout << ans;
}