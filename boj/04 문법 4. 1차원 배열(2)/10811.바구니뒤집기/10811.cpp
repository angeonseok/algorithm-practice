#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int n, m;
  cin >> n >> m;

  vector<int> arr(n);
  for(int x = 0; x < n; x++)  arr[x] = x + 1;

  for(int i = 0; i < m; i++){
    int a, b;
    cin >> a >> b;

    reverse(arr.begin() + a - 1, arr.begin() + b);
  }

  for(int j = 0; j < n; j++)  cout << arr[j] << ' ';
}