#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
  int n;
  cin >> n;

  vector<double> arr(n);
  for(int i = 0; i < n; i++)  cin >> arr[i];

  double mx = *max_element(arr.begin(), arr.end());
  for(int j = 0; j < n; j++)  arr[j] /= mx;

  double ans = 0;
  for(int k = 0; k < n; k++)  ans += (arr[k] * 100);
  
  cout << ans / n;
}