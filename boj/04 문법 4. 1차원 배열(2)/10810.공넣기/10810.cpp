#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n, m;
  cin >> n >> m;

  vector<int> arr(n, 0);
  for(int x = 0; x < m; x++){
    int i, j, k;
    cin >> i >> j >> k;

    for(int y = i - 1; y < j; y++)  arr[y] = k;
  }

  for(int a = 0; a < n; a++)  cout << arr[a] << ' ';
}